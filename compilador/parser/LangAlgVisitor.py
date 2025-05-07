# Generated from LangAlg.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LangAlgParser import LangAlgParser
else:
    from LangAlgParser import LangAlgParser

# This class defines a complete generic visitor for a parse tree produced by LangAlgParser.

class LangAlgVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LangAlgParser#programa.
    def visitPrograma(self, ctx:LangAlgParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#bloco.
    def visitBloco(self, ctx:LangAlgParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#declaracoes.
    def visitDeclaracoes(self, ctx:LangAlgParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#decl_const.
    def visitDecl_const(self, ctx:LangAlgParser.Decl_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#decl_var.
    def visitDecl_var(self, ctx:LangAlgParser.Decl_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#decl_tipo.
    def visitDecl_tipo(self, ctx:LangAlgParser.Decl_tipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#decl_proc.
    def visitDecl_proc(self, ctx:LangAlgParser.Decl_procContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#decl_func.
    def visitDecl_func(self, ctx:LangAlgParser.Decl_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#params.
    def visitParams(self, ctx:LangAlgParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#comandos.
    def visitComandos(self, ctx:LangAlgParser.ComandosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#comando.
    def visitComando(self, ctx:LangAlgParser.ComandoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#args_leia.
    def visitArgs_leia(self, ctx:LangAlgParser.Args_leiaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#lista_expr.
    def visitLista_expr(self, ctx:LangAlgParser.Lista_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#selecao.
    def visitSelecao(self, ctx:LangAlgParser.SelecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#valor_const.
    def visitValor_const(self, ctx:LangAlgParser.Valor_constContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#expressao.
    def visitExpressao(self, ctx:LangAlgParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#expr_logica.
    def visitExpr_logica(self, ctx:LangAlgParser.Expr_logicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#expr_term.
    def visitExpr_term(self, ctx:LangAlgParser.Expr_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#expr_not.
    def visitExpr_not(self, ctx:LangAlgParser.Expr_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#expr_rel.
    def visitExpr_rel(self, ctx:LangAlgParser.Expr_relContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#expr_arit.
    def visitExpr_arit(self, ctx:LangAlgParser.Expr_aritContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#termo_arit.
    def visitTermo_arit(self, ctx:LangAlgParser.Termo_aritContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#fator_arit.
    def visitFator_arit(self, ctx:LangAlgParser.Fator_aritContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#tipo.
    def visitTipo(self, ctx:LangAlgParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#tipo_basico.
    def visitTipo_basico(self, ctx:LangAlgParser.Tipo_basicoContext):
        return self.visitChildren(ctx)



del LangAlgParser