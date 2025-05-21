from compilador.lexical import get_lexer
from compilador.parser.LangAlgVisitor import LangAlgVisitor
from compilador.scope import Scope
from compilador.symbolsTable import SymbolEntry
from compilador.syntactic import get_parser

DEBUG = False

# Constantes da linguagem
valid_types = ('inteiro', 'real', 'literal', 'logico', 'registro')
invalid = 'invalid'

# Operadores por categoria
ARITMETICOS = ['+', '-', '*', '/']
RELACIONAIS_NUMERICOS = ['>', '<', '>=', '<=']
RELACIONAIS_IGUALDADE = ['=', '<>']
LOGICOS = ['e', 'ou']


class LangAlgSemantic(LangAlgVisitor):  # noqa PLR0904
    """
    Analisador semântico para a linguagem LangAlg.

    Esta classe implementa o padrão Visitor para percorrer a árvore sintática
    e realizar as verificações semânticas necessárias.
    """

    def __init__(self, output_file: str | None = None):
        self.scopes = Scope()
        self.errors = []
        self.current_function = None
        self.output_file = output_file

    def _create_file(self):
        if self.output_file:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                for e in self.errors:
                    f.write(e + '\n')
                f.write('Fim da compilacao\n')

    def visitPrograma(self, ctx):
        result = self.visitChildren(ctx)
        self._create_file()
        return result

    def addError(self, message, line):
        """Adiciona erro no formato especificado"""
        error_msg = f'Linha {line}: {message}'
        self.errors.append(error_msg)
        return invalid

    def addEntry(self, name, type, kind, line, fields=None):
        """Adiciona uma entrada na tabela de símbolos"""
        if self.scopes.searchNestedScope(name) == self.scopes.currentScope():
            self.addError(f'identificador {name} ja declarado anteriormente', line)
            return invalid
        entry = SymbolEntry(
            name=name, type=type, kind=kind, line=line, fields=fields or []
        )
        self.scopes.currentScope().symbols[name] = entry
        return type

    def visitDeclaracao_local(self, ctx):
        if DEBUG:
            print('Visit Declaracao_local: ', ctx.getText())

        if ctx.DECLARE():  # DECLARE variavel
            return self.visitVariavel(ctx.variavel())

        elif (
            ctx.CONSTANTE()
        ):  # CONSTANTE IDENT DOIS_PONTOS tipo_basico IGUAL valor_constante
            name = ctx.IDENT().getText()
            tipo = ctx.tipo_basico().getText()
            return self.addEntry(name, tipo, 'constante', ctx.start.line)

        elif ctx.TIPO():  # TIPO IDENT DOIS_PONTOS tipo
            name = ctx.IDENT().getText()
            if ctx.tipo().registro():
                fields = self.extractFields(ctx.tipo().registro(), ctx.start.line)
                return self.addEntry(name, name, 'tipo', ctx.start.line, fields)
            else:
                tipo_texto = self.processTipo(ctx.tipo(), ctx.start.line)
                return self.addEntry(name, tipo_texto, 'tipo', ctx.start.line)
        return None

    def visitDeclaracao_global(self, ctx):
        if DEBUG:
            print('Visit Declaracao_global: ', ctx.getText())
        name = ctx.IDENT().getText()
        is_function = ctx.FUNCAO() is not None

        if self.scopes.searchNestedScope(name) == self.scopes.currentScope():
            return self.addError(
                f'identificador {name} ja declarado anteriormente', ctx.start.line
            )

        # Criar novo escopo para os parâmetros
        self.scopes.createScope()

        old_function = self.current_function
        if is_function:
            self.current_function = name

        # Processar parâmetros
        params_info = []
        if ctx.parametros():
            params_info = self.visitParametros(ctx.parametros())

        # Registrar função/procedimento no escopo anterior
        kind = 'funcao' if is_function else 'procedimento'
        tipo = invalid
        if is_function and ctx.tipo_estendido():
            tipo = self.processTipo_estendido(ctx, ctx.start.line)
        elif not is_function:
            tipo = 'void'

        self.scopes.tablesList[-2].symbols[name] = SymbolEntry(
            name=name, type=tipo, kind=kind, line=ctx.start.line, fields=params_info
        )

        # Processar corpo
        self.visitCorpo(ctx.corpo())

        self.current_function = old_function

        # Sair do escopo
        self.scopes.leaveScope()

        return None

    def visitVariavel(self, ctx):
        if DEBUG:
            print('Visit Variavel: ', ctx.getText())
        identifiers = ctx.identificador()
        tipo_ctx = ctx.tipo()

        # Determinar o tipo
        tipo = self.processTipo(tipo_ctx, ctx.start.line)

        # Adicionar cada variável à tabela de símbolos
        for id_ctx in identifiers:
            name = id_ctx.IDENT(0).getText()
            if tipo == 'registro':
                fields = self.extractFields(tipo_ctx.registro(), ctx.start.line)
                self.addEntry(name, tipo, 'variavel', ctx.start.line, fields)
            else:
                self.addEntry(name, tipo, 'variavel', id_ctx.start.line)

    def visitIdentificador(self, ctx):
        if DEBUG:
            print('Visit Identificador: ', ctx.getText())
        if isinstance(ctx, list):
            ctx = ctx[0]

        if len(ctx.IDENT()) == 0:
            return invalid

        base_name = ctx.IDENT(0).getText()
        symbol_table = self.scopes.searchNestedScope(base_name)

        # Verificação 3: Identificador não declarado
        if not symbol_table:
            if len(ctx.IDENT()) != 1:
                base_name = '.'.join([id.getText() for id in ctx.IDENT()])
            return self.addError(
                f'identificador {base_name} nao declarado', ctx.start.line
            )

        entry = symbol_table.get(base_name)

        # Verificar acesso a campos de registro
        if len(ctx.IDENT()) > 1 and entry:
            tipo_atual = entry.type

            if tipo_atual != 'registro':
                # Se for um ponteiro para registro, verificar o tipo apontado
                if tipo_atual.startswith('^'):
                    tipo_atual = tipo_atual[1:]  # tratar ponteiro

                # Procurar o tipo do registro na tabela de símbolos
                if registro_table := self.scopes.searchNestedScope(tipo_atual):
                    entry = registro_table.get(tipo_atual)
                    if not entry or not entry.fields:
                        return invalid

            # Verificar acesso aos campos do registro
            campo_atual = ctx.IDENT(1).getText()
            for field in entry.fields:
                if field['name'] == campo_atual:
                    return field['type']

            # Campo não encontrado no registro
            return self.addError(
                f'identificador {base_name}.{campo_atual} nao declarado', ctx.start.line
            )

        return entry.type

    def visitParametros(self, ctx):
        """Visita os parâmetros formais e retorna informações sobre eles"""
        params_info = []

        for param_ctx in ctx.parametro():
            tipo = self.processTipo_estendido(param_ctx, param_ctx.start.line)
            is_var = param_ctx.VAR() is not None

            for id_ctx in param_ctx.identificador():
                name = id_ctx.IDENT(0).getText()
                kind = 'var_param' if is_var else 'param'
                self.addEntry(name, tipo, kind, id_ctx.start.line)
                params_info.append({'name': name, 'type': tipo, 'is_var': is_var})

        return params_info

    def visitParametro(self, ctx):
        if DEBUG:
            print('Visit Parametro: ', ctx.getText())
        tipo = self.processTipo(ctx.tipo_estendido(), ctx.start.line)

        # Adicionar parâmetros à tabela de símbolos
        for id_ctx in ctx.identificador():
            name = id_ctx.IDENT(0).getText()
            kind = 'var_param' if ctx.VAR() else 'param'
            self.addEntry(name, tipo, kind, id_ctx.start.line)

    def visitCmdChamada(self, ctx):
        """Visita uma chamada de procedimento"""
        if DEBUG:
            print('Visit CmdChamada: ', ctx.getText())

        proc_name = ctx.IDENT().getText()
        symbol_table = self.scopes.searchNestedScope(proc_name)

        if not symbol_table:
            return self.addError(
                f'identificador {proc_name} nao declarado', ctx.start.line
            )

        proc_entry = symbol_table.get(proc_name)
        if proc_entry.kind != 'procedimento':
            return self.addError(
                f'identificador {proc_name} nao e um procedimento', ctx.start.line
            )

        # Verificar compatibilidade de argumentos
        self.verifyArguments(
            ctx.expressao(), proc_entry.fields, ctx.start.line, proc_name
        )

        return None

    def visitCmdAtribuicao(self, ctx):
        if DEBUG:
            print('Visit CmdAtribuicao: ', ctx.getText())
        # Obter tipo do identificador (variável que recebe a atribuição)
        id_type = self.visitIdentificador(ctx.identificador())
        if id_type == invalid:
            return None
        # Obter tipo da expressão
        exp_type = self.visitExpressao(ctx.expressao())

        # Verificação: Atribuição não compatível
        if not self.checkCompatible(id_type, exp_type):
            var_name = ctx.identificador().getText()
            if id_type.startswith('^'):
                var_name = '^' + var_name
            self.addError(f'atribuicao nao compativel para {var_name}', ctx.start.line)
        return None

    def visitCmdRetorne(self, ctx):
        """Verifica se o comando retorne está em um contexto de função"""
        if DEBUG:
            print('Visit CmdRetorne: ', ctx.getText())

        # Verificar se estamos dentro de uma função
        if not self.current_function:
            return self.addError(
                'comando retorne nao permitido nesse escopo', ctx.start.line
            )

        # Obter o tipo da expressão retornada
        exp_type = self.visitExpressao(ctx.expressao())

        # Obter o tipo da função atual
        symbol_table = self.scopes.searchNestedScope(self.current_function)
        if not symbol_table:
            return invalid

        func_entry = symbol_table.get(self.current_function)
        if not func_entry:
            return invalid

        # Verificar compatibilidade do tipo retornado com o tipo da função
        if not self.checkCompatible(func_entry.type, exp_type):
            return self.addError(
                f'incompatibilidade de tipos no retorno de {self.current_function}',
                ctx.start.line,
            )

        return None

    def visitExpressao(self, ctx):
        if isinstance(ctx, list):
            ctx = ctx[0]

        if DEBUG:
            print('Visit Expressao: ', ctx.getText())

        tipo1 = self.visitTermo_logico(ctx.termo_logico())
        if ctx.fator_logico():
            tipo2 = self.visitFator_logico(ctx.fator_logico())
            if (tipo1 != 'logico') or (tipo2 != 'logico'):
                return invalid

        return tipo1

    def visitTermo_logico(self, ctx):
        if DEBUG:
            print('Visit Termo_logico: ', ctx.getText())
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

        if DEBUG:
            print('Visit Fator_logico: ', ctx.getText())

        tipo = self.visitParcela_logica(ctx.parcela_logica())
        if ctx.OP_NAO():
            if tipo != 'logico':
                return invalid
        return tipo

    def visitParcela_logica(self, ctx):
        if DEBUG:
            print('Visit Parcela_logica: ', ctx.getText())
        if ctx.exp_relacional():
            return self.visitExp_relacional(ctx.exp_relacional())
        return 'logico'  # VERDADEIRO ou FALSO

    def visitExp_relacional(self, ctx):
        if DEBUG:
            print('Visit Exp_relacional: ', ctx.getText())
        if isinstance(ctx, list):
            ctx = ctx[0]

        if len(ctx.exp_aritmetica()) == 1:
            return self.visitExp_aritmetica(ctx.exp_aritmetica())

        tipo1 = self.visitExp_aritmetica(ctx.exp_aritmetica(0))
        tipo2 = self.visitExp_aritmetica(ctx.exp_aritmetica(1))

        if invalid in {tipo1, tipo2}:
            return invalid

        if ctx.op_relacional().getText() in {'>', '<', '>=', '<='}:
            if (tipo1 not in {'inteiro', 'real'}) or (tipo2 not in {'inteiro', 'real'}):
                return invalid
        elif ctx.op_relacional().getText() in {'=', '<>'}:
            if not (
                (tipo1 in {'inteiro', 'real'} and tipo2 in {'inteiro', 'real'})
                or (tipo1 == tipo2)
            ):
                return invalid

        return 'logico'

    def visitExp_aritmetica(self, ctx):
        if isinstance(ctx, list):
            ctx = ctx[0]

        if DEBUG:
            print('Visit Exp_aritmetica: ', ctx.getText())

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

        if DEBUG:
            print('Visit Termo: ', ctx.getText())

        if len(ctx.fator()) == 1:
            return self.visitFator(ctx.fator())

        for fator in ctx.fator():
            tipo = self.visitFator(fator)
            if tipo not in {'inteiro', 'real'}:
                return invalid

        # Em divisões o resultado é sempre real
        return 'real'

    def visitFator(self, ctx):
        if isinstance(ctx, list):
            ctx = ctx[0]

        if DEBUG:
            print('Visit Fator: ', ctx.getText())

        if len(ctx.parcela()) == 1:
            return self.visitParcela(ctx.parcela())

        is_real = False
        for parcela in ctx.parcela():
            tipo = self.visitParcela(parcela)
            if tipo == 'real':
                is_real = True
            if tipo not in {'inteiro', 'real'}:
                return invalid

        # Se algum dos valores for real, o resultado é real
        if is_real:
            return 'real'
        else:
            return 'inteiro'

    def visitParcela(self, ctx):
        if isinstance(ctx, list):
            ctx = ctx[0]

        if DEBUG:
            print('Visit Parcela: ', ctx.getText())

        if ctx.parcela_unario():
            return self.visitParcela_unario(ctx.parcela_unario())
        elif ctx.parcela_nao_unario():
            return self.visitParcela_nao_unario(ctx.parcela_nao_unario())
        return invalid

    def visitParcela_unario(self, ctx):
        if DEBUG:
            print('Visit Parcela_unario: ', ctx.getText())
        if ctx.identificador():
            return self.visitIdentificador(ctx.identificador())
        elif ctx.NUM_INT():
            return 'inteiro'
        elif ctx.NUM_REAL():
            return 'real'
        elif ctx.IDENT():
            return self._process_call_function(ctx)
        elif exp := ctx.expressao():
            if isinstance(exp, list):
                exp = exp[0]
            return self.visitExpressao(exp)
        return invalid

    def _process_call_function(self, ctx):
        func_name = ctx.IDENT().getText()
        symbol_table = self.scopes.searchNestedScope(func_name)

        if not symbol_table:
            return self.addError(
                f'identificador {func_name} nao declarado', ctx.start.line
            )

        entry = symbol_table.get(func_name)
        if entry.kind != 'funcao':
            return self.addError(
                f'identificador {func_name} nao e uma funcao', ctx.start.line
            )

        if ctx.expressao():  # Porque aqui chama exp dnv?
            # Verificar compatibilidade de argumentos
            self.verifyArguments(
                ctx.expressao(), entry.fields, ctx.start.line, func_name
            )
        return entry.type

    def visitParcela_nao_unario(self, ctx):
        if DEBUG:
            print('Visit Parcela_nao_unario: ', ctx.getText())
        if ctx.ENDERECO():
            return '^' + self.visitIdentificador(ctx.identificador())
        elif ctx.CADEIA():
            return 'literal'
        return invalid

    def checkCompatible(self, tipo_destino, tipo_origem):
        """Verifica se a atribuição é compatível conforme as regras especificadas"""
        if DEBUG:
            print(f'Verificando compatibilidade: {tipo_destino} <- {tipo_origem}')

        # Se algum dos tipos for inválido, a atribuição não é possível
        is_valid = False

        if invalid in {tipo_destino, tipo_origem}:
            return False

        # Caso 1: ponteiro ← endereço
        if tipo_destino.startswith('^') and tipo_origem.startswith('^'):
            # Verificar se os tipos apontados são compatíveis
            tipo_apontado_destino = tipo_destino[1:]
            tipo_apontado_origem = tipo_origem[1:]
            is_valid = tipo_apontado_destino == tipo_apontado_origem

        # Caso 2: (real | inteiro) ← (real | inteiro)
        if tipo_destino in {'real', 'inteiro'} and tipo_origem in {'real', 'inteiro'}:
            is_valid = True

        # Caso 3: literal ← literal
        if tipo_destino == 'literal' and tipo_origem == 'literal':
            is_valid = True

        # Caso 4: logico ← logico
        if tipo_destino == 'logico' and tipo_origem == 'logico':
            is_valid = True

        # Caso 5: registro ← registro (mesmo nome)
        if tipo_destino == tipo_origem:
            scope_dest = self.scopes.searchNestedScope(tipo_destino)
            if scope_dest and scope_dest.get(tipo_destino):
                is_valid = True

        return is_valid

    @staticmethod
    def getResultingType(tipo1, tipo2, operador):
        """Determina o tipo resultante de uma operação entre dois tipos"""
        tipo = invalid

        # Operações aritméticas
        if operador in ARITMETICOS:
            # Operações entre tipos numéricos
            if tipo1 in {'inteiro', 'real'} and tipo2 in {'inteiro', 'real'}:
                # Se algum for real, o resultado é real
                tipo = 'real' if 'real' in {tipo1, tipo2} else 'inteiro'

            # Concatenação de strings com operador +
            if operador == '+' and tipo1 == 'literal' and tipo2 == 'literal':
                tipo = 'literal'

        # Operação módulo (%)
        elif operador == '%':
            if tipo1 == 'inteiro' and tipo2 == 'inteiro':
                tipo = 'inteiro'

        # Operações lógicas
        elif operador in LOGICOS:
            if tipo1 == 'logico' and tipo2 == 'logico':
                tipo = 'logico'

        return tipo

    def processTipo(self, tipo_ctx, line):
        """Processa um contexto de tipo e retorna o tipo correspondente"""
        if tipo_ctx.registro():
            return 'registro'
        elif tipo_ctx.tipo_estendido():
            return self.processTipo_estendido(tipo_ctx, line)
        return invalid

    def processTipo_estendido(self, tipo_ctx, line):
        tipo_text = tipo_ctx.tipo_estendido().getText()
        # Verificar tipo ponteiro
        is_pointer = tipo_text.startswith('^')
        if is_pointer:
            tipo_text = tipo_text[1:]  # Remove o ^ do início

        # Verificar se é um tipo básico ou um tipo definido pelo usuário
        if tipo_text in valid_types:
            tipo = tipo_text
        else:
            # Verificar se o tipo foi declarado
            symbol_table = self.scopes.searchNestedScope(tipo_text)
            if not symbol_table or not symbol_table.get(tipo_text):
                self.addError(f'tipo {tipo_text} nao declarado', line)
                tipo = invalid
            else:
                tipo = tipo_text

        # Adicionar o ^ de volta se for ponteiro
        if is_pointer:
            tipo = '^' + tipo

        return tipo

    def verifyArguments(self, expressoes_ctx, params_formais, line, nome_subprograma):
        """Verifica se os argumentos são compatíveis com os parâmetros formais"""
        if expressoes_ctx is None:
            expressoes_ctx = []

        # Verificar número de argumentos
        if len(expressoes_ctx) != len(params_formais):
            return self.addError(
                f'incompatibilidade de parametros na chamada de {nome_subprograma}',
                line,
            )

        # Verificar tipo de cada argumento
        for i, exp_ctx in enumerate(expressoes_ctx):
            arg_tipo = self.visitExpressao(exp_ctx)
            param_tipo = params_formais[i]['type']

            if param_tipo != arg_tipo:
                return self.addError(
                    f'incompatibilidade de parametros na chamada de {nome_subprograma}',
                    line,
                )

        return None

    def extractFields(self, registro_ctx, line):
        """Extrai os campos de um tipo de registro"""
        fields = []
        if registro_ctx.variavel():
            for var in registro_ctx.variavel():
                field_tipo = self.processTipo(var.tipo(), line)
                for id_ctx in var.identificador():
                    field_name = id_ctx.IDENT(0).getText()
                    fields.append({'name': field_name, 'type': field_tipo})
        return fields


def run_semantic_analysis(input_file: str, output_file: str):
    lexer = get_lexer(input_file)
    tree = get_parser(lexer).programa()
    semantic = LangAlgSemantic(output_file)
    semantic.visitPrograma(tree)

    return semantic.errors
