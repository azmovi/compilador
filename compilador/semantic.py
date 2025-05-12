from compilador.parser.LangAlgVisitor import LangAlgVisitor
from compilador.scope import Scope
from compilador.symbolsTable import SymbolEntry

DEBUG = False

# Lista de tipos válidos na linguagem
valid_types = ('inteiro', 'real', 'literal', 'logico', 'registro')
invalid = 'invalid'

class LangAlgSemantic(LangAlgVisitor):
    def __init__(self):
        self.scopes = Scope()
        self.errors = []
    
    def visitPrograma(self, ctx, output_file):
        result = self.visitChildren(ctx)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                for e in self.errors:
                    f.write(e + '\n')
                f.write('Fim da compilacao\n')
        
        return result
    
    def addError(self, message, line):
        """Adiciona erro no formato especificado"""
        error_msg = f"Linha {line}: {message}"
        self.errors.append(error_msg)
        return invalid
    
    def addEntry(self, name, type_str, kind, line, fields=None):
        """Adiciona uma entrada na tabela de símbolos"""
        if self.scopes.searchNestedScope(name) == self.scopes.currentScope():
            self.addError(f"identificador {name} ja declarado anteriormente", line)
            return invalid
        entry = SymbolEntry(name=name, type=type_str, kind=kind, line=line, fields=fields or [])
        self.scopes.currentScope().symbols[name] = entry  # Adiciona diretamente à tabela
        return type_str
    
    # Visite declarações locais
    def visitDeclaracao_local(self, ctx):
        if DEBUG: print("Visit Declaracao_local: ", ctx.getText())
        if ctx.DECLARE():
            return self.visitVariavel(ctx.variavel())
        elif ctx.CONSTANTE():
            name = ctx.IDENT().getText()
            tipo = ctx.tipo_basico().getText()
            return self.addEntry(name, tipo, 'constante', ctx.start.line)
        elif ctx.TIPO():
            name = ctx.IDENT().getText()
            if ctx.tipo().registro():
                return self.addEntry(name, 'registro', 'tipo', ctx.start.line)
            else:
                tipo_texto = ctx.tipo().getText()
                return self.addEntry(name, tipo_texto, 'tipo', ctx.start.line)
        return None
    
    # Visite declarações globais
    def visitDeclaracao_global(self, ctx):
        if DEBUG: print("Visit Declaracao_global: ", ctx.getText())
        name = ctx.IDENT().getText()
        is_function = ctx.FUNCAO() is not None
        
        # Criar novo escopo para os parâmetros
        self.scopes.createScope()
        
        # Processar parâmetros
        if ctx.parametros():
            self.visitParametros(ctx.parametros())
        
        # Registrar função/procedimento no escopo anterior
        kind = 'funcao' if is_function else 'procedimento'
        tipo = ctx.tipo_estendido().getText() if is_function and ctx.tipo_estendido() else 'void'
        
        # Verificar se o tipo de retorno existe (apenas para funções)
        if is_function and tipo not in valid_types and tipo != 'void':
            symbol_table = self.scopes.searchNestedScope(tipo)
            if not symbol_table or not symbol_table.get(tipo):
                self.addError(f"tipo {tipo} nao declarado", ctx.start.line)
        
        self.scopes.tablesList[-2].symbols[name] = SymbolEntry(
            name=name, type=tipo, kind=kind, line=ctx.start.line
        )
        
        # Processar corpo
        self.visitCorpo(ctx.corpo())
        
        # Sair do escopo
        self.scopes.leaveScope()
        
        return None
    
    def visitVariavel(self, ctx):
        if DEBUG: print("Visit Variavel: ", ctx.getText())
        identifiers = ctx.identificador()
        tipo_ctx = ctx.tipo()
        
        # Determinar o tipo
        if tipo_ctx.registro():
            tipo = 'registro'
        elif tipo_ctx.tipo_estendido():
            tipo_text = tipo_ctx.tipo_estendido().getText()
            # Verificar se é um tipo básico ou um tipo definido pelo usuário
            if tipo_text in valid_types:
                tipo = tipo_text
            else:
                # Verificar se o tipo foi declarado
                symbol_table = self.scopes.searchNestedScope(tipo_text)
                if not symbol_table or not symbol_table.get(tipo_text):
                    self.addError(f"tipo {tipo_text} nao declarado", tipo_ctx.start.line)
                    tipo = invalid
                else:
                    tipo = tipo_text
        else:
            tipo = invalid
        
        # Adicionar cada variável à tabela de símbolos
        for id_ctx in identifiers:
            name = id_ctx.IDENT(0).getText()
            self.addEntry(name, tipo, 'variavel', id_ctx.start.line)
        
        return None
    
    def visitIdentificador(self, ctx):
        if DEBUG: print("Visit Identificador: ", ctx.getText())
        if isinstance(ctx, list):
            ctx = ctx[0]
            
        if len(ctx.IDENT()) == 0:
            return invalid
        
        base_name = ctx.IDENT(0).getText()
        symbol_table = self.scopes.searchNestedScope(base_name)
        
        # Verificação 3: Identificador não declarado
        if not symbol_table:
            return self.addError(f"identificador {base_name} nao declarado", ctx.start.line)
        
        entry = symbol_table.get(base_name)
        return entry.type
    
    def visitParametro(self, ctx):
        if DEBUG: print("Visit Parametro: ", ctx.getText())
        tipo = ctx.tipo_estendido().getText()
        
        # Verificar se o tipo existe
        if tipo not in valid_types:
            symbol_table = self.scopes.searchNestedScope(tipo)
            if not symbol_table or not symbol_table.get(tipo):
                self.addError(f"tipo {tipo} nao declarado", ctx.start.line)
        
        # Adicionar parâmetros à tabela de símbolos
        for id_ctx in ctx.identificador():
            name = id_ctx.IDENT(0).getText()
            kind = 'var_param' if ctx.VAR() else 'param'
            self.addEntry(name, tipo, kind, id_ctx.start.line)
        
        return None
    
    def visitCmdAtribuicao(self, ctx):
        if DEBUG: print("Visit CmdAtribuicao: ", ctx.getText())
        # Obter tipo do identificador (variável que recebe a atribuição)
        id_type = self.visitIdentificador(ctx.identificador())
        # Obter tipo da expressão
        exp_type = self.visitExpressao(ctx.expressao())
        
        # Verificação 4: Atribuição não compatível
        if not self.checkCompatible(id_type, exp_type):
            var_name = ctx.identificador().getText()
            self.addError(f"atribuicao nao compativel para {var_name}", ctx.start.line)
        return None
    
    def visitExpressao(self, ctx):
        if isinstance(ctx, list):
            ctx = ctx[0]

        if DEBUG: print("Visit Expressao: ", ctx.getText())

        tipo1 = self.visitTermo_logico(ctx.termo_logico())
        if ctx.fator_logico():
            tipo2 = self.visitFator_logico(ctx.fator_logico())
            if (tipo1 != 'logico') or (tipo2 != 'logico'):
                return invalid 
            
        return tipo1
    
    def visitTermo_logico(self, ctx):
        if DEBUG: print("Visit Termo_logico: ", ctx.getText())
        if isinstance(ctx, list):
            ctx = ctx[0]
            
        if len(ctx.fator_logico()) == 1:
            return self.visitFator_logico(ctx.fator_logico(0))
        
        for fator in ctx.fator_logico():
            if self.visitFator_logico(fator) != 'logico':
                return invalid
        return 'logico'
        
    
    def visitFator_logico(self, ctx):
        if isinstance(ctx, list):
            ctx = ctx[0]
        
        if DEBUG: print("Visit Fator_logico: ", ctx.getText())
        
        tipo = self.visitParcela_logica(ctx.parcela_logica())
        if ctx.OP_NAO():
            if tipo != 'logico':
                return invalid
        return tipo
    
    def visitParcela_logica(self, ctx):
        if DEBUG: print("Visit Parcela_logica: ", ctx.getText())
        if ctx.exp_relacional():
            return self.visitExp_relacional(ctx.exp_relacional())
        return 'logico'  # VERDADEIRO ou FALSO
    
    def visitExp_relacional(self, ctx):
        if DEBUG: print("Visit Exp_relacional: ", ctx.getText())
        if isinstance(ctx, list):
            ctx = ctx[0]
            
        if len(ctx.exp_aritmetica()) == 1:
            return self.visitExp_aritmetica(ctx.exp_aritmetica())
        
        tipo1 = self.visitExp_aritmetica(ctx.exp_aritmetica(0))
        tipo2 = self.visitExp_aritmetica(ctx.exp_aritmetica(1))
        
        
        if tipo1 == invalid or tipo2 == invalid:
            return invalid
        
        if ctx.op_relacional().getText() in ['>', '<', '>=', '<=']:
            if (tipo1 not in ['inteiro', 'real']) or (tipo2 not in ['inteiro', 'real']):
                return invalid
        elif ctx.op_relacional().getText() in ['=', '<>']:
            if not ((tipo1 in ['inteiro', 'real'] and tipo2 in ['inteiro', 'real']) or
                    (tipo1 == tipo2)):
                return invalid
        
        return 'logico'
        
    def visitExp_aritmetica(self, ctx):
        if isinstance(ctx, list):
            ctx = ctx[0]
        
        if DEBUG: print("Visit Exp_aritmetica: ", ctx.getText())

        termos = ctx.termo()
        if len(termos) == 1:
            return self.visitTermo(termos[0])
        
        tipo_resultante = self.visitTermo(termos[0])
        
        for i in range(1, len(termos)):
            tipo_atual = self.visitTermo(termos[i])
            op = ctx.op1(i - 1).getText() 
            
            tipo_resultante = self.getResultingType(tipo_resultante, tipo_atual, op)
            if tipo_resultante == invalid:
                break
        return tipo_resultante
            
    
    def visitTermo(self, ctx):
        if isinstance(ctx, list):
            ctx = ctx[0]
        
        if DEBUG: print("Visit Termo: ", ctx.getText())
            
        if len(ctx.fator()) == 1:
            return self.visitFator(ctx.fator())
        
        for fator in ctx.fator():
            tipo = self.visitFator(fator)
            if tipo not in ['inteiro', 'real']:
                return invalid

        # Em divisões o resultado é sempre real
        return 'real'
    
    def visitFator(self, ctx):
        if isinstance(ctx, list):
            ctx = ctx[0]
            
        if DEBUG: print("Visit Fator: ", ctx.getText())
        
        if len(ctx.parcela()) == 1:
            return self.visitParcela(ctx.parcela())
        
        is_real = False
        for parcela in ctx.parcela():
            tipo = self.visitParcela(parcela)
            if tipo == 'real':
                is_real = True
            if tipo not in ['inteiro', 'real']:
                return invalid
        
        # Se algum dos valores for real, o resultado é real
        if is_real:
            return 'real'
        else:
            return 'inteiro'
    
    def visitParcela(self, ctx):
        if isinstance(ctx, list):
            ctx = ctx[0]
        
        if DEBUG: print("Visit Parcela: ", ctx.getText())
            
        if ctx.parcela_unario():
            return self.visitParcela_unario(ctx.parcela_unario())
        elif ctx.parcela_nao_unario():
            return self.visitParcela_nao_unario(ctx.parcela_nao_unario())
        return invalid

    def visitParcela_unario(self, ctx):
        if DEBUG: print("Visit Parcela_unario: ", ctx.getText())
        if ctx.identificador():
            return self.visitIdentificador(ctx.identificador())
        elif ctx.NUM_INT():
            return 'inteiro'
        elif ctx.NUM_REAL():
            return 'real'
        elif ctx.IDENT():  # chamada de função
            func_name = ctx.IDENT().getText()
            symbol_table = self.scopes.searchNestedScope(func_name)
            
            if not symbol_table:
                return self.addError(f"identificador {func_name} nao declarado", ctx.start.line)
            
            entry = symbol_table.get(func_name)
            if entry.kind != 'funcao':
                return self.addError(f"identificador {func_name} nao e uma funcao", ctx.start.line)
            
            return entry.type
        elif ctx.expressao():
            return self.visitExpressao(ctx.expressao())
        return invalid

    def visitParcela_nao_unario(self, ctx):
        if DEBUG: print("Visit Parcela_nao_unario: ", ctx.getText())
        if ctx.ENDERECO():
            return "^" + self.visitIdentificador(ctx.identificador())
        elif ctx.CADEIA():
            return 'literal'
        return invalid
    
    # Método auxiliar para verificar compatibilidade de tipos
    def checkCompatible(self, tipo_destino, tipo_origem):
        if DEBUG: print(f"Verificando compatibilidade: {tipo_destino} <- {tipo_origem}")
        """Verifica se a atribuição é compatível conforme as regras especificadas"""
        # Se algum dos tipos for inválido, a atribuição não é possível
        if tipo_destino == invalid or tipo_origem == invalid:
            return False
        
        # Caso 1: ponteiro ← endereço
        if tipo_destino.startswith('^') and tipo_origem.startswith('^'):
            return True
        
        # Caso 2: (real | inteiro) ← (real | inteiro)
        if tipo_destino in ('real', 'inteiro') and tipo_origem in ('real', 'inteiro'):
            # Não permitir atribuição de real para inteiro
            if tipo_destino == 'inteiro' and tipo_origem == 'real':
                return False
            return True
        
        # Caso 3: literal ← literal
        if tipo_destino == 'literal' and tipo_origem == 'literal':
            return True
        
        # Caso 4: logico ← logico
        if tipo_destino == 'logico' and tipo_origem == 'logico':
            return True
        
        # Caso 5: registro ← registro (mesmo nome)
        if tipo_destino == 'registro' and tipo_origem == 'registro':
            return True
        
        # Se não se encaixa em nenhum caso, não é compatível
        return False
    
    def getResultingType(self, tipo1, tipo2, operador):
        """Determina o tipo resultante de uma operação entre dois tipos"""
        if tipo1 == invalid or tipo2 == invalid:
            return invalid
        
        # Operações aritméticas
        if operador in ['+', '-', '*', '/']:
            # Operações entre tipos numéricos
            if tipo1 in ['inteiro', 'real'] and tipo2 in ['inteiro', 'real']:
                # Se algum for real, o resultado é real
                return 'real' if 'real' in [tipo1, tipo2] else 'inteiro'
            
            # Concatenação de strings com operador +
            if operador == '+' and tipo1 == 'literal' and tipo2 == 'literal':
                return 'literal'
            return invalid
        
        # Operação módulo (%)
        if operador == '%':
            if tipo1 == 'inteiro' and tipo2 == 'inteiro':
                return 'inteiro'
            return invalid
        
        # Operações lógicas
        if operador in ['e', 'ou']:
            if tipo1 == 'logico' and tipo2 == 'logico':
                return 'logico'            
            return invalid
        
        return invalid

def run_semantic_analysis(input_file: str, output_file: str):
    from compilador.lexical import get_lexer
    from compilador.syntactic import get_parser
    
    lexer = get_lexer(input_file)
    tree = get_parser(lexer).programa()
    semantic = LangAlgSemantic()
    semantic.visitPrograma(tree, output_file)
    
    return semantic.errors