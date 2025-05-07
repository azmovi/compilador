from compilador.parser.LangAlgVisitor import LangAlgVisitor
from compilador.scope import Scope
from compilador.symbolsTable import SymbolicTable
from compilador.syntactic import get_parser

class LangAlgSemantic(LangAlgVisitor):
    def __init__(self):
        self.scopes = Scope()
        self.errors: list[str] = []

    def visitPrograma(self, ctx):
        super().visitPrograma(ctx)
        for e in self.errors:
            print(e)
        print("Fim da compilação")
        return None

    def visitDecl_const(self, ctx):
        # CONSTANTE IDENT DOIS_PONTOS tipo_basico ATRIB expressao
        name = ctx.IDENT().getText()
        if self.nestedScopes[0].check()
        return super().visitDecl_const(ctx)

    def visitDecl_var(self, ctx):
        # DECLARE IDENT (VIRGULA IDENT)* DOIS_PONTOS tipo
        return super().visitDecl_var(ctx)
    
    def visitDecl_tipo(self, ctx):
        # TIPO IDENT DOIS_PONTOS REGISTRO decl_var* FIM_REGISTRO
        return super().visitDecl_tipo(ctx)
    
    def visitDecl_proc(self, ctx):
        # PROCEDIMENTO IDENT params? bloco FIM_PROCEDIMENTO
        return super().visitDecl_proc(ctx)
    
    def visitDecl_func(self, ctx):
        # FUNCAO IDENT params? DOIS_PONTOS tipo bloco FIM_FUNCAO
        return super().visitDecl_func(ctx)


def run_semantic_analysis():
    tree =  get_parser().programa()
    semantic = LangAlgSemantic()
    semantic.visitPrograma(tree)

