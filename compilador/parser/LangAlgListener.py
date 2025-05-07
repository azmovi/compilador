# Generated from LangAlg.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LangAlgParser import LangAlgParser
else:
    from LangAlgParser import LangAlgParser

# This class defines a complete listener for a parse tree produced by LangAlgParser.
class LangAlgListener(ParseTreeListener):

    # Enter a parse tree produced by LangAlgParser#programa.
    def enterPrograma(self, ctx:LangAlgParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#programa.
    def exitPrograma(self, ctx:LangAlgParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#bloco.
    def enterBloco(self, ctx:LangAlgParser.BlocoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#bloco.
    def exitBloco(self, ctx:LangAlgParser.BlocoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#declaracoes.
    def enterDeclaracoes(self, ctx:LangAlgParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by LangAlgParser#declaracoes.
    def exitDeclaracoes(self, ctx:LangAlgParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by LangAlgParser#decl_const.
    def enterDecl_const(self, ctx:LangAlgParser.Decl_constContext):
        pass

    # Exit a parse tree produced by LangAlgParser#decl_const.
    def exitDecl_const(self, ctx:LangAlgParser.Decl_constContext):
        pass


    # Enter a parse tree produced by LangAlgParser#decl_var.
    def enterDecl_var(self, ctx:LangAlgParser.Decl_varContext):
        pass

    # Exit a parse tree produced by LangAlgParser#decl_var.
    def exitDecl_var(self, ctx:LangAlgParser.Decl_varContext):
        pass


    # Enter a parse tree produced by LangAlgParser#decl_tipo.
    def enterDecl_tipo(self, ctx:LangAlgParser.Decl_tipoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#decl_tipo.
    def exitDecl_tipo(self, ctx:LangAlgParser.Decl_tipoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#decl_proc.
    def enterDecl_proc(self, ctx:LangAlgParser.Decl_procContext):
        pass

    # Exit a parse tree produced by LangAlgParser#decl_proc.
    def exitDecl_proc(self, ctx:LangAlgParser.Decl_procContext):
        pass


    # Enter a parse tree produced by LangAlgParser#decl_func.
    def enterDecl_func(self, ctx:LangAlgParser.Decl_funcContext):
        pass

    # Exit a parse tree produced by LangAlgParser#decl_func.
    def exitDecl_func(self, ctx:LangAlgParser.Decl_funcContext):
        pass


    # Enter a parse tree produced by LangAlgParser#params.
    def enterParams(self, ctx:LangAlgParser.ParamsContext):
        pass

    # Exit a parse tree produced by LangAlgParser#params.
    def exitParams(self, ctx:LangAlgParser.ParamsContext):
        pass


    # Enter a parse tree produced by LangAlgParser#comandos.
    def enterComandos(self, ctx:LangAlgParser.ComandosContext):
        pass

    # Exit a parse tree produced by LangAlgParser#comandos.
    def exitComandos(self, ctx:LangAlgParser.ComandosContext):
        pass


    # Enter a parse tree produced by LangAlgParser#comando.
    def enterComando(self, ctx:LangAlgParser.ComandoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#comando.
    def exitComando(self, ctx:LangAlgParser.ComandoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#args_leia.
    def enterArgs_leia(self, ctx:LangAlgParser.Args_leiaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#args_leia.
    def exitArgs_leia(self, ctx:LangAlgParser.Args_leiaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#lista_expr.
    def enterLista_expr(self, ctx:LangAlgParser.Lista_exprContext):
        pass

    # Exit a parse tree produced by LangAlgParser#lista_expr.
    def exitLista_expr(self, ctx:LangAlgParser.Lista_exprContext):
        pass


    # Enter a parse tree produced by LangAlgParser#selecao.
    def enterSelecao(self, ctx:LangAlgParser.SelecaoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#selecao.
    def exitSelecao(self, ctx:LangAlgParser.SelecaoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#valor_const.
    def enterValor_const(self, ctx:LangAlgParser.Valor_constContext):
        pass

    # Exit a parse tree produced by LangAlgParser#valor_const.
    def exitValor_const(self, ctx:LangAlgParser.Valor_constContext):
        pass


    # Enter a parse tree produced by LangAlgParser#expressao.
    def enterExpressao(self, ctx:LangAlgParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#expressao.
    def exitExpressao(self, ctx:LangAlgParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#expr_logica.
    def enterExpr_logica(self, ctx:LangAlgParser.Expr_logicaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#expr_logica.
    def exitExpr_logica(self, ctx:LangAlgParser.Expr_logicaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#expr_term.
    def enterExpr_term(self, ctx:LangAlgParser.Expr_termContext):
        pass

    # Exit a parse tree produced by LangAlgParser#expr_term.
    def exitExpr_term(self, ctx:LangAlgParser.Expr_termContext):
        pass


    # Enter a parse tree produced by LangAlgParser#expr_not.
    def enterExpr_not(self, ctx:LangAlgParser.Expr_notContext):
        pass

    # Exit a parse tree produced by LangAlgParser#expr_not.
    def exitExpr_not(self, ctx:LangAlgParser.Expr_notContext):
        pass


    # Enter a parse tree produced by LangAlgParser#expr_rel.
    def enterExpr_rel(self, ctx:LangAlgParser.Expr_relContext):
        pass

    # Exit a parse tree produced by LangAlgParser#expr_rel.
    def exitExpr_rel(self, ctx:LangAlgParser.Expr_relContext):
        pass


    # Enter a parse tree produced by LangAlgParser#expr_arit.
    def enterExpr_arit(self, ctx:LangAlgParser.Expr_aritContext):
        pass

    # Exit a parse tree produced by LangAlgParser#expr_arit.
    def exitExpr_arit(self, ctx:LangAlgParser.Expr_aritContext):
        pass


    # Enter a parse tree produced by LangAlgParser#termo_arit.
    def enterTermo_arit(self, ctx:LangAlgParser.Termo_aritContext):
        pass

    # Exit a parse tree produced by LangAlgParser#termo_arit.
    def exitTermo_arit(self, ctx:LangAlgParser.Termo_aritContext):
        pass


    # Enter a parse tree produced by LangAlgParser#fator_arit.
    def enterFator_arit(self, ctx:LangAlgParser.Fator_aritContext):
        pass

    # Exit a parse tree produced by LangAlgParser#fator_arit.
    def exitFator_arit(self, ctx:LangAlgParser.Fator_aritContext):
        pass


    # Enter a parse tree produced by LangAlgParser#tipo.
    def enterTipo(self, ctx:LangAlgParser.TipoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#tipo.
    def exitTipo(self, ctx:LangAlgParser.TipoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#tipo_basico.
    def enterTipo_basico(self, ctx:LangAlgParser.Tipo_basicoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#tipo_basico.
    def exitTipo_basico(self, ctx:LangAlgParser.Tipo_basicoContext):
        pass



del LangAlgParser