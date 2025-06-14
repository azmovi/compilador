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

        self.scopes.createScope()

        super().visitChildren(ctx)

        self._create_file()

        return self.code

    def visitCorpo(self, ctx: LangAlgParser.ProgramaContext):
        self.code.append("int main() {\n")

        super().visitCorpo(ctx)

        self.code.append("return 0;\n}")

    def visitDeclaracao_local(self, ctx):
        if ctx.DECLARE():
            return self.visitVariavel(ctx.variavel())
        else:
            print('caiu aqui')
            #__import__('ipdb').set_trace()

    def visitVariavel(self, variavel_context: LangAlgParser.VariavelContext):
        identificadores = variavel_context.identificador()
        tipo_variavel_context = variavel_context.tipo()

        tipo = self.get_tipo(tipo_variavel_context)

        names = []
        for identificador in identificadores:
            name = identificador.getText()
            names.append(name)
            self.addEntry(name, tipo, 'variavel', identificador.start.line)
        self.code.append(', '.join(names) + ';\n')

    def visitCmdAtribuicao(self, ctx):
        nome_var = ctx.identificador()
        self.code.append(f'{nome_var} = ')
        self.visitExp_aritmetica(ctx.expressao())
        self.code.append(';\n')

    def visitCmdSe(self, ctx):
        self.code.append('if(')
        self.visitExp_relacional(ctx.expressao())
        self.code.append(')\n')

        self.visitComando(ctx.comando(0))

        if len(ctx.cmd()) > 1:
            self.code.append('else\n')
            self.visitCmd(ctx.cmd(1))

    def visitCmdLeia(self, cmd_leia: LangAlgParser.CmdLeiaContext):
        identificadores = cmd_leia.identificador()

        if len(identificadores) > 1:
            print('caiu aqui')
            #__import__('ipdb').set_trace()

        variavel_nome = identificadores[0].getText()
        c_type = self.get_c_type(variavel_nome)
        self.code.append(f'scanf("%{c_type}", &{variavel_nome});\n')

    def visitCmdEscreva(self, cmd_escreva: LangAlgParser.CmdEscrevaContext):
        exp_contexts = cmd_escreva.expressao()

        if len(exp_contexts) > 1:
            print('caiu aqui')
            #__import__('ipdb').set_trace()

        exp_context = exp_contexts[0]
        variavel_nome = exp_context.getText()
        c_type = self.get_c_type(variavel_nome)

        self.code.append(f'printf("%{c_type}", {variavel_nome});\n')

    def visitCmdEnquanto(self, ctx):
        self.code.append('while(')
        self.visitExp_relacional(ctx.expressao())
        self.code.append(')\n')
        self.visitCmd(ctx.cmd())

    def get_tipo(self, tipo_context: LangAlgParser.TipoContext):
        tipos = {'inteiro': 'int '}
        tipo_nome = tipo_context.getText()
        self.code.append(tipos[tipo_nome])
        return tipo_nome

    def get_c_type(self, variavel_nome: str):
        #  TODO: Validar para alem do escopo corrente
        c_types = {'inteiro': 'd', 'real': 'f', 'literal': 's'}
        current_scope = self.scopes.currentScope()
        tipo = current_scope.symbols[variavel_nome].type
        return c_types[tipo]

def run_code_generation(input_file, output_file):
    lexer = get_lexer(input_file)
    tree = get_parser(lexer).programa()
    code_gen = CodeGen(output_file)
    xpto = code_gen.visitPrograma(tree)
    return xpto
