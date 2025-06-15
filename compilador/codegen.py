from compilador.lexical import get_lexer
from compilador.parser.LangAlgParser import LangAlgParser
from compilador.parser.LangAlgVisitor import LangAlgVisitor
from compilador.scope import Scope
from compilador.symbolsTable import SymbolEntry
from compilador.syntactic import get_parser

INVALID = 'invalid'


class CodeGen(LangAlgVisitor):
    def __init__(self, output_file: str):
        self.code = []
        self.output_file = output_file
        self.scopes = Scope()

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
            self.addError(f'identificador {name} ja declarado anteriormente', line)
            return INVALID
        entry = SymbolEntry(
            name=name, type=type, kind=kind, line=line, fields=fields or []
        )
        self.scopes.currentScope().symbols[name] = entry
        return type

    def visitPrograma(self, ctx: LangAlgParser.ProgramaContext):
        self.code.append('#include <stdio.h>\n')
        self.code.append('#include <stdlib.h>\n')

        self.scopes.createScope()

        super().visitChildren(ctx)

        # __import__('ipdb').set_trace()
        self._create_file()

        return self.code

    def visitCorpo(self, ctx: LangAlgParser.ProgramaContext):
        self.code.append('int main() {\n')

        super().visitCorpo(ctx)

        self.code.append('return 0;\n}')

    def visitDeclaracao_local(self, ctx):
        if ctx.DECLARE():
            return self.visitVariavel(ctx.variavel())
        else:
            # __import__('ipdb').set_trace()
            print('declaraçao local')

    def visitVariavel(self, variavel_context: LangAlgParser.VariavelContext):
        identificadores = variavel_context.identificador()
        tipo_variavel_context = variavel_context.tipo()

        tipo = self.get_tipo(tipo_variavel_context)

        names = []
        for identificador in identificadores:
            name = identificador.getText()
            names.append(name)
            self.addEntry(name, tipo, 'variavel', identificador.start.line)
        if tipo == 'literal':
            self.code.append(', '.join([f'{name}[80]' for name in names]) + ';\n')
        else:
            self.code.append(', '.join(names) + ';\n')

    def visitCmdAtribuicao(self, cmd_atribuicao: LangAlgParser.CmdAtribuicaoContext):
        nome_var, exp = cmd_atribuicao.getText().split('<-')
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
            self.code.append(f'gets({variavel_nome});\n')
        else:
            self.code.append(f'scanf("%{c_type}", &{variavel_nome});\n')

        super().visitCmdLeia(cmd_leia)

    def visitCmdEscreva(self, cmd_escreva: LangAlgParser.CmdEscrevaContext):
        expressoes = cmd_escreva.expressao()
        fmt_string = 'printf("'

        for expressao in expressoes:
            nome = expressao.getText()
            c_type = self.get_c_type(nome)

            if c_type == 'new_line':
                fmt_string += 'printf("\\n");\n'
            elif c_type == 'texto':
                fmt_string += nome[1:-1]
                if len(expressoes) == 1:
                    fmt_string += '");\n'
            else:
                if c_type == 'exp_aritmetica':
                    c_type = self.get_c_type(nome[0])
                fmt_string += f'%{c_type}", {nome});\n'
        self.code.append(fmt_string)

    def visitCmdEnquanto(self, ctx):
        self.code.append('while(')
        self.visitExp_relacional(ctx.expressao())
        self.code.append(')\n')
        self.visitCmd(ctx.cmd())

    def visitCmdPara(self, cmd_para: LangAlgParser.CmdParaContext):
        exp_aritmetica = cmd_para.exp_aritmetica()
        variavel = cmd_para.IDENT().getText()
        inicio, fim = [exp.getText() for exp in exp_aritmetica]
        fmt_string = (
            f'for ({variavel} = {inicio}; {variavel} <= {fim}; {variavel}++){{\n'
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

    def visitItem_selecao(self, item_selecao: LangAlgParser.Item_selecaoContext):
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

    def get_tipo(self, tipo_context: LangAlgParser.TipoContext):
        tipos = {'inteiro': 'int ', 'real': 'float ', 'literal': 'char '}
        tipo_nome = tipo_context.getText()
        self.code.append(tipos[tipo_nome])
        return tipo_nome

    def get_c_type(self, variavel_nome: str):
        #  TODO: Validar para alem do escopo corrente
        c_types = {
            'inteiro': 'd',
            'real': 'f',
            'literal': 's',
            '"\\n"': 'new_line',
        }
        if current_scope := self.scopes.searchNestedScope(variavel_nome):
            tipo = current_scope.symbols.get(variavel_nome)
            return c_types[tipo.type]

        elif '"' in variavel_nome:
            return c_types.get(variavel_nome, 'texto')

        else:
            return 'exp_aritmetica'

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
