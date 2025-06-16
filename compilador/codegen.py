from compilador.lexical import get_lexer
from compilador.parser.LangAlgParser import LangAlgParser
from compilador.parser.LangAlgVisitor import LangAlgVisitor
from compilador.scope import Scope
from compilador.symbolsTable import SymbolEntry
from compilador.syntactic import get_parser

INVALID = 'invalid'
valid_types = ('inteiro', 'real', 'literal', 'logico', 'registro')


class CodeGen(LangAlgVisitor):  # noqa PLR0904
    def __init__(self, output_file: str):
        self.code = []
        self.output_file = output_file
        self.scopes = Scope()
        self.ponteiro = False

    def _create_file(self):
        if self.output_file:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                for e in self.code:
                    f.write(e)

    def addError(self, message, line):
        """Adiciona erro no formato especificado"""
        error_msg = f'Linha {line}: {message}'
        self.errors.append(error_msg)
        return INVALID

    def addEntry(self, name, type, kind, line, fields=None):
        """Adiciona uma entrada na tabela de símbolos"""
        if self.scopes.searchNestedScope(name) == self.scopes.currentScope():
            self.addError(
                f'identificador {name} ja declarado anteriormente', line
            )
            return INVALID
        entry = SymbolEntry(
            name=name, type=type, kind=kind, line=line, fields=fields or []
        )
        self.scopes.currentScope().symbols[name] = entry
        return type

    def visitPrograma(self, ctx: LangAlgParser.ProgramaContext):
        self.code.append('#include <stdio.h>\n')
        self.code.append('#include <stdlib.h>\n')
        self.code.append('#include <string.h>\n')

        self.scopes.createScope()

        super().visitChildren(ctx)

        # __import__('ipdb').set_trace()
        self._create_file()

        return self.code

    def visitCorpo(self, ctx: LangAlgParser.ProgramaContext):
        self.code.append('int main() {\n')

        super().visitCorpo(ctx)

        self.code.append('return 0;\n}')

    def visitDeclaracao_local(
        self, declaracao_local: LangAlgParser.Declaracao_localContext
    ):
        if declaracao_local.DECLARE():
            return self.visitVariavel(declaracao_local.variavel())

        elif declaracao_local.CONSTANTE():
            name = declaracao_local.IDENT().getText()
            tipo = declaracao_local.tipo_basico().getText()
            constante = declaracao_local.valor_constante().getText()
            self.code.append(f'#define {name} {constante}\n')
            return self.addEntry(
                name, tipo, 'constante', declaracao_local.start.line
            )
        elif declaracao_local.TIPO():
            name = declaracao_local.IDENT().getText()
            tipo = declaracao_local.tipo()
            fields = self.extractFields(
                tipo.registro(), declaracao_local.start.line
            )
            return self.addEntry(
                name, name, 'tipo', declaracao_local.start.line, fields
            )
        else:
            __import__('ipdb').set_trace()
            print('declaraçao local')

    def visitVariavel(self, variavel_context: LangAlgParser.VariavelContext):
        identificadores = variavel_context.identificador()
        tipo_variavel_context = variavel_context.tipo()

        tipo = self.get_tipo(tipo_variavel_context)

        if tipo == 'registro':
            identificador = identificadores[0]
            registro = tipo_variavel_context.registro()
            if registro:
                for var in registro.variavel():
                    self.visitVariavel(var)
                self.code.append(
                    '} '
                    f'{identificador.getText()};\n'
                )
        else:
            names = []
            for identificador in identificadores:
                name = identificador.getText()
                names.append(name)
                self.addEntry(name, tipo, 'variavel', identificador.start.line)
            if tipo == 'literal':
                self.code.append(
                    ', '.join([f'{name}[80]' for name in names]) + ';\n'
                )
            else:
                self.code.append(', '.join(names) + ';\n')

    def visitCmdAtribuicao(
        self, cmd_atribuicao: LangAlgParser.CmdAtribuicaoContext
    ):
        nome_var, exp = cmd_atribuicao.getText().split('<-')

        if '.' in nome_var:
            nome_real = nome_var.split('.')[1]
            table = self.scopes.searchNestedScope(nome_real)
            if table:
                tipo = table.get(nome_real).type
                if tipo == 'literal':
                    self.code.append(f'strcpy( {nome_var},{exp});\n')
                else:
                    self.code.append(f'{nome_var} = {exp};\n')
        else:
            if self.ponteiro:
                nome_var = nome_var.replace('^', '*')

            self.code.append(f'{nome_var} = {exp};\n')

    def visitCmdSe(self, cmd_se: LangAlgParser.CmdSeContext):
        expressao = cmd_se.expressao()
        self.code.append(f'if ({self._tratar_expressao(expressao)}) {{\n')
        stmts = cmd_se.cmd()
        if_stmt = stmts[0]
        super().visitCmd(if_stmt)

        if len(stmts) > 1:
            else_stmt = stmts[1]
            self.code.append('} else {\n')
            super().visitCmd(else_stmt)

        self.code.append('}\n')

    def visitCmdLeia(self, cmd_leia: LangAlgParser.CmdLeiaContext):
        identificadores = cmd_leia.identificador()

        if len(identificadores) > 1:
            __import__('ipdb').set_trace()
            print('cmd leia')

        identificador = identificadores[0]
        variavel_nome = identificador.getText()
        c_type = self.get_c_type(variavel_nome)
        if c_type == 's':
            self.code.append(
                f'fgets({variavel_nome}, sizeof({variavel_nome}), stdin);\n'
             )
        else:
            self.code.append(f'scanf("%{c_type}", &{variavel_nome});\n')

        super().visitCmdLeia(cmd_leia)

    def visitCmdEscreva(self, cmd_escreva: LangAlgParser.CmdEscrevaContext):
        expressoes = cmd_escreva.expressao()

        for expressao in expressoes:
            nome = expressao.getText()
            c_type = self.get_c_type(nome)

            if self.code[-1][-1] == '\n':
                fmt_string = 'printf("'
            else:
                fmt_string = ''

            if c_type == 'new_line':
                fmt_string += '\\n");\n'

            elif c_type == 'texto':
                real_nome = nome[1:-1]
                if expressao == expressoes[0]:
                    fmt_string += real_nome
                    if len(expressoes) == 1:
                        fmt_string += '");\n'
                else:
                    fmt_string += f'{real_nome}");\n'

            elif c_type == 'exp_aritmetica':
                c_type = self.get_c_type(nome[0])
                fmt_string += f'%{c_type}", {nome});\n'

            else:
                fmt_string += f'%{c_type}", {nome});\n'

            if fmt_string != 'printf("':
                self.code.append(fmt_string)

    def visitCmdEnquanto(self, cmd_enquanto: LangAlgParser.CmdEnquantoContext):
        expressao = cmd_enquanto.expressao().getText()
        self.code.append(
            f'while ({expressao}) '
            '{\n'
        )
        for cmd in cmd_enquanto.cmd():
            super().visitCmd(cmd)

        self.code.append('}\n')

    def visitCmdPara(self, cmd_para: LangAlgParser.CmdParaContext):
        exp_aritmetica = cmd_para.exp_aritmetica()
        variavel = cmd_para.IDENT().getText()
        inicio, fim = [exp.getText() for exp in exp_aritmetica]
        fmt_string = (
            f'for ({variavel} = {inicio}; {variavel} <= {fim}; {variavel}++)'
            '{\n'
        )
        self.code.append(fmt_string)
        super().visitCmdPara(cmd_para)
        self.code.append('};\n')

    def visitCmdCaso(self, cmd_caso: LangAlgParser.CmdCasoContext):
        exp_aritmetica = cmd_caso.exp_aritmetica().getText()
        self.code.append(f'switch ({exp_aritmetica}) {{\n')

        super().visitSelecao(cmd_caso.selecao())

        if cmd := cmd_caso.cmd():
            self.code.append('default:\n')
            super().visitCmd(cmd[0])
        self.code.append('}\n')

    def visitItem_selecao(
        self, item_selecao: LangAlgParser.Item_selecaoContext
    ):
        constantes = item_selecao.constantes()
        intervalo = constantes.getText().split('..')

        if len(intervalo) > 1:
            inicio, fim = intervalo
            for i in range(int(inicio), int(fim) + 1):
                self.code.append(f'case {i}:\n')
        else:
            inicio = intervalo[0]
            self.code.append(f'case {inicio}:\n')

        super().visitItem_selecao(item_selecao)
        self.code.append('break;\n')

    def visitCmdFaca(self, cmd_faca: LangAlgParser.CmdFacaContext):
        expressao = self._tratar_expressao(cmd_faca.expressao())

        self.code.append('do {\n')

        for cmd in cmd_faca.cmd():
            super().visitCmd(cmd)

        self.code.append(
            '} while ('
            f'{expressao});\n'
        )

    def get_tipo(self, tipo_context: LangAlgParser.TipoContext):
        tipos = {'inteiro': 'int ', 'real': 'float ', 'literal': 'char '}
        tipo_nome = tipo_context.getText()

        if tipo_context.registro():
            self.code.append('struct {\n')
            return 'registro'

        if '^' in tipo_nome:
            self.ponteiro = True
            tipo_nome = tipo_nome[1:]

        if c_type := tipos.get(tipo_nome):
            fmt_string = f'{c_type} {"*" if self.ponteiro else ""}'
            self.code.append(fmt_string)
            return tipo_nome
        else:
            return 'registro'

    def get_c_type(self, variavel_nome: str):
        #  TODO: Validar para alem do escopo corrente
        c_types = {
            'inteiro': 'd',
            'real': 'f',
            'literal': 's',
            '"\\n"': 'new_line',
        }

        if '.' in variavel_nome:
            variavel_nome = variavel_nome.split('.')[1]

        if current_scope := self.scopes.searchNestedScope(variavel_nome):
            tipo = current_scope.symbols.get(variavel_nome)
            return c_types[tipo.type]

        elif '"' in variavel_nome:
            return c_types.get(variavel_nome, 'texto')

        else:
            return 'exp_aritmetica'

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

    def processTipo(self, tipo_ctx, line):
        """Processa um contexto de tipo e retorna o tipo correspondente"""
        if tipo_ctx.registro():
            return 'registro'
        elif tipo_ctx.tipo_estendido():
            return self.processTipo_estendido(tipo_ctx, line)
        return 'invalid'

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
                tipo = 'invalid'
            else:
                tipo = tipo_text

        # Adicionar o ^ de volta se for ponteiro
        if is_pointer:
            tipo = '^' + tipo

        return tipo

    @staticmethod
    def _tratar_expressao(expressao: LangAlgParser.ExpressaoContext):
        expr = expressao.getText()
        expr = expr.replace('=', '==')
        expr = expr.replace('nao', '!')
        expr = expr.replace('ou', '||')
        expr = expr.replace('e', '&&')
        return expr


def run_code_generation(input_file, output_file):
    lexer = get_lexer(input_file)
    tree = get_parser(lexer).programa()
    code_gen = CodeGen(output_file)
    xpto = code_gen.visitPrograma(tree)
    return xpto
