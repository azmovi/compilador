from compilador.parser.LangAlgParser import LangAlgParser
from compilador.parser.LangAlgVisitor import LangAlgVisitor
from compilador.symbolsTable import SymbolEntry
from compilador.semantic import LangAlgSemantic

class LAGeradorC(LangAlgVisitor):
    def __init__(self):
        self.saida = []
        self.tabela = SymbolEntry()
        self.semantica = LangAlgSemantic(self.tabela)

    def visitPrograma(self, ctx):
        self.saida.append("#include <stdio.h>\n")
        self.saida.append("#include <stdlib.h>\n")
        self.saida.append("\n")

        for dec in ctx.declaracao():
            self.visitDeclaracao_global(dec)

        self.saida.append("\n")
        self.saida.append("int main() {\n")

        for cmd in ctx.comando():
            self.visitComando(cmd)

        self.saida.append("\n")
        return None

    def visitDeclaracao_global(self, ctx):
        nome_var = ctx.VARIAVEL().getText()
        tipo_var = ctx.TIPO_VAR().getText()

        if tipo_var == "INTEIRO":
            tipo_var = "int"
        elif tipo_var == "REAL":
            tipo_var = "float"
        elif tipo_var == "LITERAL":
            tipo_var = "int"
        elif tipo_var == "CADEIA":
            tipo_var = "char*"

        self.saida.append(f"{tipo_var} {nome_var};\n")
        return None

    def visitDeclaracao_local(self, ctx):
        nome_var = ctx.VARIAVEL().getText()
        tipo_var = ctx.TIPO_VAR().getText()

        if tipo_var == "INTEIRO":
            tipo_var = "int"
        elif tipo_var == "REAL":
            tipo_var = "float"
        elif tipo_var == "LITERAL":
            tipo_var = "int"
        elif tipo_var == "CADEIA":
            tipo_var = "char*"

        self.saida.append(f"{tipo_var} {nome_var};\n")
        return None
    
    def visitCmdAtribuicao(self, ctx):
        nome_var = ctx.identificador()
        self.saida.append(f"{nome_var} = ")
        self.visitExp_aritmetica(ctx.expressao())
        self.saida.append(";\n")
        return None
    
    def visitCmdSe(self, ctx):
        self.saida.append("if(")
        self.visitExp_relacional(ctx.expressao())
        self.saida.append(")\n")

        self.visitComando(ctx.comando(0))

        if len(ctx.cmd()) > 1:
            self.saida.append("else\n")
            self.visitCmd(ctx.cmd(1))

        return None
    
    def visitCmdLeia(self, ctx):
        nome_var = ctx.identificador()
        self.saida.append(f'scanf("%d", &{nome_var});\n')
        return None
    
    def visitCmdEscreva(self, ctx):
        self.saida.append(f'printf("%d", {ctx.expressao()});\n')
        return None
    
    def visitCmdAtribuicao(self, ctx):
        nome_var = ctx.identificador()
        self.saida.append(f"{nome_var} = ")
        self.visitExp_aritmetica(ctx.expressao())
        self.saida.append(";\n")
        return None
    
    def visitCmdEnquanto(self, ctx):
        self.saida.append("while(")
        self.visitExp_relacional(ctx.expressao())
        self.saida.append(")\n")
        self.visitCmd(ctx.cmd())
        return None

