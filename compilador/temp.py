from compilador.parser.LangAlgVisitor import LangAlgVisitor
from compilador.scope import Scope
from compilador.symbolsTable import SymbolEntry
from compilador.parser.LangAlgParser import LangAlgParser

invalid = 'invalido'
class LangAlgSemantic(LangAlgVisitor):
    def __init__(self):
        self.scopes = Scope()
        self.errors = []
        self.current_function = None  # Para controle de retorno em funções
        self.inside_loop = False      # Para controle de comandos dentro de loops

    def visitPrograma(self, ctx, output_file=None):
        result = self.visitChildren(ctx)
        
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                for e in self.errors:
                    f.write(e + '\n')
                f.write('Fim da compilacao\n')
        
        return result

    def addError(self, message, line):
        error_msg = f"Linha {line}: {message}"
        self.errors.append(error_msg)
        return invalid

    def addEntry(self, name, type_str, kind, line, fields=None):
        entry = SymbolEntry(name=name, type=type_str, kind=kind, line=line, fields=fields)
        self.scopes.currentScope().add(name, entry)
        return type_str

    def visitDeclaracao_local(self, ctx):
        if ctx.DECLARE():
            return self.visitVariavel(ctx.variavel())
        elif ctx.CONSTANTE():
            name = ctx.IDENT().getText()
            tipo = self.visitTipo_basico(ctx.tipo_basico())
            
            # Verifica compatibilidade do tipo com o valor
            if tipo != self.getTypeFromValue(ctx.valor_constante()):
                self.addError(f"atribuicao nao compativel para {name}", ctx.start.line)
                return invalid
            
            return self.addEntry(name, tipo, 'constante', ctx.start.line)
        elif ctx.TIPO():
            name = ctx.IDENT().getText()
            tipo = self.visitTipo(ctx.tipo())
            return self.addEntry(name, tipo, 'tipo', ctx.start.line)
        
        return self.visitChildren(ctx)

    def visitDeclaracao_global(self, ctx):
        is_function = ctx.FUNCAO() is not None
        name = ctx.IDENT().getText()
        line = ctx.start.line
        
        # Criar novo escopo para os parâmetros
        self.scopes.createScope()
        
        # Salvar função atual para verificar retornos
        old_function = self.current_function
        if is_function:
            return_type = self.visitTipo_estendido(ctx.tipo_estendido()) if ctx.tipo_estendido() else invalid
            self.current_function = {'name': name, 'type': return_type}
        else:
            self.current_function = {'name': name, 'type': None}  # Procedimento não tem retorno
        
        # Processar parâmetros
        params_types = []
        if ctx.parametros():
            params_types = self.visitParametros(ctx.parametros())
        
        # Registrar função/procedimento no escopo anterior
        kind = 'funcao' if is_function else 'procedimento'
        self.scopes.tablesList[-2].add(name, SymbolEntry(
            name=name,
            type=return_type if is_function else 'void',
            kind=kind,
            line=line,
            fields=params_types
        ))
        
        # Processar corpo
        self.visitCorpo(ctx.corpo())
        
        # Restaurar função anterior e sair do escopo
        self.current_function = old_function
        self.scopes.leaveScope()
        
        return None

    def visitVariavel(self, ctx):
        identifiers = ctx.identificador()
        tipo = self.visitTipo(ctx.tipo())
        
        for id_ctx in identifiers:
            name = id_ctx.IDENT(0).getText()
            self.addEntry(name, tipo, 'variavel', id_ctx.start.line)
        
        return None

    def visitIdentificador(self, ctx):
        if len(ctx.IDENT()) == 0:
            return invalid
        
        base_name = ctx.IDENT(0).getText()
        symbol_table = self.scopes.searchNestedScope(base_name)
        
        if not symbol_table:
            return self.addError(f"identificador {base_name} nao declarado", ctx.start.line)
        
        entry = symbol_table.get(base_name)
        
        # Verificar acesso a campos de registro
        if len(ctx.IDENT()) > 1 and entry.type != 'registro':
            return self.addError(f"{base_name} não é um registro", ctx.start.line)
        
        # TODO: implementar verificação de campos de registro e dimensões
        
        # Verificar dimensões (arrays)
        if ctx.dimensao() and ctx.dimensao().exp_aritmetica():
            for exp in ctx.dimensao().exp_aritmetica():
                if self.visitExp_aritmetica(exp) not in ['inteiro']:
                    return self.addError("expressão não-inteira em indexação", exp.start.line)
        
        return entry.type

    def visitTipo(self, ctx):
        if ctx.registro():
            return self.visitRegistro(ctx.registro())
        return self.visitTipo_estendido(ctx.tipo_estendido())

    def visitTipo_basico(self, ctx):
        return ctx.getText()

    def visitTipo_estendido(self, ctx):
        is_pointer = ctx.PONTEIRO() is not None
        
        if ctx.tipo_basico():
            base_type = self.visitTipo_basico(ctx.tipo_basico())
        else:  # IDENT - tipo nomeado
            type_name = ctx.IDENT().getText()
            symbol_table = self.scopes.searchNestedScope(type_name)
            
            if not symbol_table:
                return self.addError(f"tipo {type_name} nao declarado", ctx.start.line)
            
            entry = symbol_table.get(type_name)
            if entry.kind != 'tipo':
                return self.addError(f"{type_name} não é um tipo", ctx.start.line)
            
            base_type = entry.type
        
        # Se for ponteiro, indica isso no tipo
        return f"^{base_type}" if is_pointer else base_type

    def visitRegistro(self, ctx):
        # Registros têm seus próprios campos
        fields = []
        
        for var_ctx in ctx.variavel():
            identifiers = var_ctx.identificador()
            tipo = self.visitTipo(var_ctx.tipo())
            
            for id_ctx in identifiers:
                name = id_ctx.IDENT(0).getText()
                fields.append((name, tipo))
        
        return 'registro'

    def getTypeFromValue(self, ctx):
        if ctx.CADEIA():
            return 'literal'
        elif ctx.NUM_INT():
            return 'inteiro'
        elif ctx.NUM_REAL():
            return 'real'
        elif ctx.VERDADEIRO() or ctx.FALSO():
            return 'logico'
        return invalid

    def visitValor_constante(self, ctx):
        return self.getTypeFromValue(ctx)

    def visitParametro(self, ctx):
        is_var = ctx.VAR() is not None
        tipo = self.visitTipo_estendido(ctx.tipo_estendido())
        params = []
        
        for id_ctx in ctx.identificador():
            name = id_ctx.IDENT(0).getText()
            kind = 'var_param' if is_var else 'param'
            self.addEntry(name, tipo, kind, id_ctx.start.line)
            params.append((name, tipo, kind))
        
        return params

    def visitParametros(self, ctx):
        params = []
        for param_ctx in ctx.parametro():
            params.extend(self.visitParametro(param_ctx))
        return params

    def visitCmd(self, ctx):
        return self.visitChildren(ctx)

    # def visitCmdLeia(self, ctx):
    #     for id_ctx in ctx.identificador():
    #         tipo = self.visitIdentificador(id_ctx)
    #         if tipo == invalid:
    #             continue
                
    #         # Variáveis em leia devem ser variáveis ou parâmetros
    #         name = id_ctx.IDENT(0).getText()
    #         symbol_table = self.scopes.searchNestedScope(name)
    #         if symbol_table:
    #             entry = symbol_table.get(name)
    #             if entry.kind not in ['variavel', 'param', 'var_param']:
    #                 self.addError(f"identificador {name} não é uma variável", id_ctx.start.line)
        
    #     return None

    # def visitCmdEscreva(self, ctx):
    #     for exp_ctx in ctx.expressao():
    #         tipo = self.visitExpressao(exp_ctx)
    #         if tipo not in ['inteiro', 'real', 'literal', 'logico']:
    #             self.addError("expressão inválida em comando 'escreva'", exp_ctx.start.line)
        
    #     return None

    # def visitCmdSe(self, ctx):
    #     # Verificar se a expressão da condição é do tipo lógico
    #     cond_type = self.visitExpressao(ctx.expressao())
    #     if cond_type != 'logico' and cond_type != invalid:
    #         self.addError("expressão do comando 'se' deve ser do tipo logico", ctx.expressao().start.line)
        
    #     # Visitar os blocos então e senão
    #     for cmd_ctx in ctx.cmd():
    #         self.visitCmd(cmd_ctx)
        
    #     return None

    # def visitCmdCaso(self, ctx):
    #     # Verificar se a expressão do caso é do tipo inteiro
    #     exp_type = self.visitExp_aritmetica(ctx.exp_aritmetica())
    #     if exp_type != 'inteiro' and exp_type != invalid:
    #         self.addError("expressão do comando 'caso' deve ser do tipo inteiro", ctx.exp_aritmetica().start.line)
        
    #     # Visitar a seleção e o bloco senão
    #     self.visitSelecao(ctx.selecao())
        
    #     for cmd_ctx in ctx.cmd():
    #         self.visitCmd(cmd_ctx)
        
    #     return None

    # def visitCmdPara(self, ctx):
    #     # Verificar se a variável de controle existe e é do tipo inteiro
    #     var_name = ctx.IDENT().getText()
    #     symbol_table = self.scopes.searchNestedScope(var_name)
        
    #     if not symbol_table:
    #         self.addError(f"variável de controle {var_name} não declarada", ctx.IDENT().getSymbol().line)
    #     else:
    #         entry = symbol_table.get(var_name)
    #         if entry.kind != 'variavel':
    #             self.addError(f"'{var_name}' não é uma variável", ctx.IDENT().getSymbol().line)
    #         elif entry.type != 'inteiro':
    #             self.addError(f"variável de controle {var_name} deve ser do tipo inteiro", ctx.IDENT().getSymbol().line)
        
    #     # Verificar as expressões de início e fim
    #     inicio_type = self.visitExp_aritmetica(ctx.exp_aritmetica(0))
    #     if inicio_type != 'inteiro' and inicio_type != invalid:
    #         self.addError("expressão de início do laço 'para' deve ser do tipo inteiro", ctx.exp_aritmetica(0).start.line)
        
    #     fim_type = self.visitExp_aritmetica(ctx.exp_aritmetica(1))
    #     if fim_type != 'inteiro' and fim_type != invalid:
    #         self.addError("expressão de fim do laço 'para' deve ser do tipo inteiro", ctx.exp_aritmetica(1).start.line)
        
    #     # Marcar que estamos dentro de um loop e visitar os comandos
    #     old_inside_loop = self.inside_loop
    #     self.inside_loop = True
        
    #     for cmd_ctx in ctx.cmd():
    #         self.visitCmd(cmd_ctx)
        
    #     self.inside_loop = old_inside_loop
        
    #     return None

    # def visitCmdEnquanto(self, ctx):
    #     # Verificar se a expressão da condição é do tipo lógico
    #     cond_type = self.visitExpressao(ctx.expressao())
    #     if cond_type != 'logico' and cond_type != invalid:
    #         self.addError("expressão do comando 'enquanto' deve ser do tipo logico", ctx.expressao().start.line)
        
    #     # Marcar que estamos dentro de um loop e visitar os comandos
    #     old_inside_loop = self.inside_loop
    #     self.inside_loop = True
        
    #     for cmd_ctx in ctx.cmd():
    #         self.visitCmd(cmd_ctx)
        
    #     self.inside_loop = old_inside_loop
        
    #     return None

    # def visitCmdFaca(self, ctx):
    #     # Verificar se a expressão da condição é do tipo lógico
    #     cond_type = self.visitExpressao(ctx.expressao())
    #     if cond_type != 'logico' and cond_type != invalid:
    #         self.addError("expressão do comando 'ate' deve ser do tipo logico", ctx.expressao().start.line)
        
    #     # Marcar que estamos dentro de um loop e visitar os comandos
    #     old_inside_loop = self.inside_loop
    #     self.inside_loop = True
        
    #     for cmd_ctx in ctx.cmd():
    #         self.visitCmd(cmd_ctx)
        
    #     self.inside_loop = old_inside_loop
        
    #     return None

    # def visitCmdAtribuicao(self, ctx):
    #     # Obter o tipo da variável que está recebendo a atribuição
    #     is_pointer = ctx.PONTEIRO() is not None
    #     id_type = self.visitIdentificador(ctx.identificador())
        
    #     if id_type == invalid:
    #         return invalid
        
    #     # Se for atribuição a um ponteiro (^var <- valor)
    #     if is_pointer and not id_type.startswith('^'):
    #         self.addError(f"'{ctx.identificador().getText()}' não é um ponteiro", ctx.start.line)
    #         return invalid
        
    #     # Se for atribuição ao conteúdo de um ponteiro, ajustar o tipo esperado
    #     if is_pointer:
    #         id_type = id_type[1:]  # Remove o ^ do tipo
        
    #     # Verificar tipo da expressão
    #     exp_type = self.visitExpressao(ctx.expressao())
    #     if exp_type == invalid or id_type == invalid:
    #         return invalid
        
    #     # Verificar compatibilidade de tipos
    #     if not self.areTipesCompativeis(id_type, exp_type):
    #         self.addError(f"incompatibilidade de tipos na atribuição", ctx.start.line)
    #         return invalid
        
    #     return None

    # def visitCmdChamada(self, ctx):
    #     func_name = ctx.IDENT().getText()
    #     symbol_table = self.scopes.searchNestedScope(func_name)
        
    #     if not symbol_table:
    #         return self.addError(f"subrotina '{func_name}' não declarada", ctx.start.line)
        
    #     entry = symbol_table.get(func_name)
    #     if entry.kind not in ['funcao', 'procedimento']:
    #         return self.addError(f"'{func_name}' não é uma subrotina", ctx.start.line)
        
    #     # Verificar número de argumentos
    #     expected_params = entry.fields
    #     actual_params = ctx.expressao()
        
    #     if len(expected_params) != len(actual_params):
    #         return self.addError(f"incompatibilidade de parâmetros na chamada de '{func_name}'", ctx.start.line)
        
    #     # Verificar tipos dos argumentos
    #     for i, (exp_ctx, (_, param_type, param_kind)) in enumerate(zip(actual_params, expected_params)):
    #         arg_type = self.visitExpressao(exp_ctx)
            
    #         # Verificar compatibilidade de tipos
    #         if not self.areTipesCompativeis(param_type, arg_type):
    #             self.addError(f"incompatibilidade de tipos no parâmetro {i+1} da chamada de '{func_name}'", exp_ctx.start.line)
            
    #         # Verificar passagem por referência (var)
    #         if param_kind == 'var_param':
    #             # Se o parâmetro é por referência, o argumento deve ser uma variável
    #             if not isinstance(exp_ctx, LangAlgParser.ExpressaoContext) or not exp_ctx.termo_logico() or len(exp_ctx.termo_logico()) != 1:
    #                 self.addError(f"parâmetro {i+1} de '{func_name}' espera uma variável (passagem por referência)", exp_ctx.start.line)
        
    #     return entry.type if entry.kind == 'funcao' else None

    # def visitCmdRetorne(self, ctx):
    #     # Verificar se estamos dentro de uma função
    #     if not self.current_function:
    #         return self.addError("comando 'retorne' fora de função ou procedimento", ctx.start.line)
        
    #     if self.current_function['type'] is None:  # Procedimento
    #         return self.addError("comando 'retorne' em procedimento", ctx.start.line)
        
    #     # Verificar tipo do retorno
    #     exp_type = self.visitExpressao(ctx.expressao())
    #     if not self.areTipesCompativeis(self.current_function['type'], exp_type):
    #         self.addError(f"tipo de retorno incompatível com tipo da função", ctx.start.line)
        
    #     return None

    def visitSelecao(self, ctx):
        for item in ctx.item_selecao():
            self.visitItem_selecao(item)
        return None

    def visitItem_selecao(self, ctx):
        self.visitConstantes(ctx.constantes())
        for cmd_ctx in ctx.cmd():
            self.visitCmd(cmd_ctx)
        return None

    def visitConstantes(self, ctx):
        for intervalo in ctx.numero_intervalo():
            self.visitNumero_intervalo(intervalo)
        return None

    def visitNumero_intervalo(self, ctx):
        # Nada a verificar aqui, os números já são inteiros pela gramática
        return None

    def visitExp_aritmetica(self, ctx):
        if not ctx.termo():
            return invalid
        
        result_type = self.visitTermo(ctx.termo(0))
        
        for i, op in enumerate(ctx.op1()):
            term_type = self.visitTermo(ctx.termo(i + 1))
            result_type = self.getResultingType(result_type, term_type, op.getText())
        
        return result_type

    def visitTermo(self, ctx):
        if not ctx.fator():
            return invalid
        
        result_type = self.visitFator(ctx.fator(0))
        
        for i, op in enumerate(ctx.op2()):
            fator_type = self.visitFator(ctx.fator(i + 1))
            result_type = self.getResultingType(result_type, fator_type, op.getText())
        
        return result_type

    def visitFator(self, ctx):
        if not ctx.parcela():
            return invalid
        
        result_type = self.visitParcela(ctx.parcela(0))
        
        for i, _ in enumerate(ctx.op3()):
            parcela_type = self.visitParcela(ctx.parcela(i + 1))
            # O operador % só funciona entre inteiros
            if result_type != 'inteiro' or parcela_type != 'inteiro':
                self.addError("operador '%' aplicável apenas a inteiros", ctx.op3(i).start.line)
                return invalid
        
        return result_type

    def visitParcela(self, ctx):
        if ctx.parcela_unario():
            tipo = self.visitParcela_unario(ctx.parcela_unario())
            # Se houver operador unário, verificar se o tipo é numérico
            if ctx.op_unario() and tipo not in ['inteiro', 'real']:
                self.addError("operador unário aplicável apenas a tipos numéricos", ctx.start.line)
                return invalid
            return tipo
        else:
            return self.visitParcela_nao_unario(ctx.parcela_nao_unario())

    def visitParcela_unario(self, ctx):
        if ctx.identificador():
            # Acesso a variável ou campo
            is_pointer = ctx.PONTEIRO() is not None
            id_type = self.visitIdentificador(ctx.identificador())
            
            # Se for acesso a ponteiro (^var)
            if is_pointer:
                if not id_type.startswith('^'):
                    self.addError(f"'{ctx.identificador().getText()}' não é um ponteiro", ctx.start.line)
                    return invalid
                return id_type[1:]  # Retorna o tipo sem o ^
            
            return id_type
        
        elif ctx.IDENT():  # Chamada de função
            return self.visitCmdChamada(ctx)
        
        elif ctx.NUM_INT():
            return 'inteiro'
        
        elif ctx.NUM_REAL():
            return 'real'
        
        elif ctx.expressao():  # Expressão entre parênteses
            return self.visitExpressao(ctx.expressao())
        
        return invalid

    def visitParcela_nao_unario(self, ctx):
        if ctx.ENDERECO():
            # Operador & (endereço) - retorna um ponteiro para o tipo
            id_type = self.visitIdentificador(ctx.identificador())
            if id_type == invalid:
                return invalid
            return f"^{id_type}"
        
        elif ctx.CADEIA():
            return 'literal'
        
        return invalid

    def visitExp_relacional(self, ctx):
        if not ctx.exp_aritmetica():
            return invalid
        
        exp1_type = self.visitExp_aritmetica(ctx.exp_aritmetica(0))
        
        # Se não houver operador relacional, retorna o tipo da expressão
        if not ctx.op_relacional():
            return exp1_type
        
        # Com operador relacional, o resultado é sempre lógico
        exp2_type = self.visitExp_aritmetica(ctx.exp_aritmetica(1))
        
        # Verificar compatibilidade dos operandos
        op = ctx.op_relacional().getText()
        # Para operadores = e <>, todos os tipos são permitidos
        if op in ['=', '<>']:
            if not self.areTipesCompativeis(exp1_type, exp2_type):
                self.addError(f"operandos incompatíveis para o operador '{op}'", ctx.op_relacional().start.line)
                return invalid
        # Para outros operadores (<, >, <=, >=), apenas tipos numéricos são permitidos
        else:
            if exp1_type not in ['inteiro', 'real'] or exp2_type not in ['inteiro', 'real']:
                self.addError(f"operador '{op}' aplicável apenas a tipos numéricos", ctx.op_relacional().start.line)
                return invalid
        
        return 'logico'

    def visitExpressao(self, ctx):
        # Verificação mais flexível para lidar com diferentes formas de contexto
        if isinstance(ctx, list):
            # Se for uma lista, pegar o primeiro elemento
            if not ctx:
                return invalid
            ctx = ctx[0]
        
        # Acessar termo_logico de forma mais flexível
        termos = ctx.termo_logico() if hasattr(ctx, 'termo_logico') else []
        
        if not termos:
            return invalid
        
        result_type = self.visitTermo_logico(termos)
        
        # Acessar operadores de forma mais flexível
        op_logicos = ctx.op_logico_1() if hasattr(ctx, 'op_logico_1') else []
        
        # Se houver operadores 'ou', verificar se todos são do tipo lógico
        for i, _ in enumerate(op_logicos):
            # Verificar se há um próximo termo
            if i + 1 < len(termos):
                term_type = self.visitTermo_logico(termos[i + 1])
                
                if result_type != 'logico' or term_type != 'logico':
                    self.addError("operador 'ou' aplicável apenas a tipos logico", op_logicos[i].start.line)
                    return invalid
        
        return result_type

    def visitTermo_logico(self, ctx):
        # Verificação mais flexível para lidar com diferentes formas de contexto
        if isinstance(ctx, list):
            # Se for uma lista, pegar o primeiro elemento
            if not ctx:
                return invalid
            ctx = ctx[0]
        
        # Acessar fator_logico de forma mais flexível
        fatores = ctx.fator_logico() if hasattr(ctx, 'fator_logico') else []
        
        if not fatores:
            return invalid
        
        result_type = self.visitFator_logico(fatores[0])
        
        # Acessar operadores de forma mais flexível
        op_logicos = ctx.op_logico_2() if hasattr(ctx, 'op_logico_2') else []
        
        # Se houver operadores 'e', verificar se todos são do tipo lógico
        for i, _ in enumerate(op_logicos):
            # Verificar se há um próximo fator
            if i + 1 < len(fatores):
                fator_type = self.visitFator_logico(fatores[i + 1])
                
                if result_type != 'logico' or fator_type != 'logico':
                    self.addError("operador 'e' aplicável apenas a tipos logico", op_logicos[i].start.line)
                    return invalid
        
        return result_type

    def visitFator_logico(self, ctx):
        tipo = self.visitParcela_logica(ctx.parcela_logica())
        
        # Se houver operador 'nao', verificar se o tipo é lógico
        if ctx.OP_NAO() and tipo != 'logico':
            self.addError("operador 'nao' aplicável apenas a tipos logico", ctx.OP_NAO().getSymbol().line)
            return invalid
        
        return tipo

    def visitParcela_logica(self, ctx):
        if ctx.exp_relacional():
            return self.visitExp_relacional(ctx.exp_relacional())
        else:  # VERDADEIRO ou FALSO
            return 'logico'

    # Métodos auxiliares
    def areTipesCompativeis(self, tipo1, tipo2):
        """Verifica se os tipos são compatíveis para atribuição e operações"""
        if tipo1 == invalid or tipo2 == invalid:
            return False
        
        # Tipos idênticos são compatíveis
        if tipo1 == tipo2:
            return True
        
        # Inteiro pode ser atribuído a real
        if tipo1 == 'real' and tipo2 == 'inteiro':
            return True
        
        # Verificar compatibilidade de ponteiros
        if tipo1.startswith('^') and tipo2 == 'inteiro' and tipo2 == 0:  # NULL pode ser atribuído a qualquer ponteiro
            return True
        
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
            
            self.addError(f"operador '{operador}' não aplicável aos tipos '{tipo1}' e '{tipo2}'", -1)
            return invalid
        
        # Operação módulo (%)
        if operador == '%':
            if tipo1 == 'inteiro' and tipo2 == 'inteiro':
                return 'inteiro'
            
            self.addError(f"operador '%' aplicável apenas a inteiros", -1)
            return invalid
        
        # Operações lógicas
        if operador in ['e', 'ou']:
            if tipo1 == 'logico' and tipo2 == 'logico':
                return 'logico'
            
            self.addError(f"operador '{operador}' aplicável apenas a tipos logico", -1)
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