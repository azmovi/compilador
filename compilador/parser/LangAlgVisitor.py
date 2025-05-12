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


    # Visit a parse tree produced by LangAlgParser#corpo.
    def visitCorpo(self, ctx:LangAlgParser.CorpoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#declaracao_local.
    def visitDeclaracao_local(self, ctx:LangAlgParser.Declaracao_localContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#declaracao_global.
    def visitDeclaracao_global(self, ctx:LangAlgParser.Declaracao_globalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#variavel.
    def visitVariavel(self, ctx:LangAlgParser.VariavelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#identificador.
    def visitIdentificador(self, ctx:LangAlgParser.IdentificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#dimensao.
    def visitDimensao(self, ctx:LangAlgParser.DimensaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#tipo.
    def visitTipo(self, ctx:LangAlgParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#tipo_basico.
    def visitTipo_basico(self, ctx:LangAlgParser.Tipo_basicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#tipo_estendido.
    def visitTipo_estendido(self, ctx:LangAlgParser.Tipo_estendidoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#valor_constante.
    def visitValor_constante(self, ctx:LangAlgParser.Valor_constanteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#registro.
    def visitRegistro(self, ctx:LangAlgParser.RegistroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#parametro.
    def visitParametro(self, ctx:LangAlgParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#parametros.
    def visitParametros(self, ctx:LangAlgParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#cmd.
    def visitCmd(self, ctx:LangAlgParser.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#cmdLeia.
    def visitCmdLeia(self, ctx:LangAlgParser.CmdLeiaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#cmdEscreva.
    def visitCmdEscreva(self, ctx:LangAlgParser.CmdEscrevaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#cmdSe.
    def visitCmdSe(self, ctx:LangAlgParser.CmdSeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#cmdCaso.
    def visitCmdCaso(self, ctx:LangAlgParser.CmdCasoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#cmdPara.
    def visitCmdPara(self, ctx:LangAlgParser.CmdParaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#cmdEnquanto.
    def visitCmdEnquanto(self, ctx:LangAlgParser.CmdEnquantoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#cmdFaca.
    def visitCmdFaca(self, ctx:LangAlgParser.CmdFacaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#cmdAtribuicao.
    def visitCmdAtribuicao(self, ctx:LangAlgParser.CmdAtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#cmdChamada.
    def visitCmdChamada(self, ctx:LangAlgParser.CmdChamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#cmdRetorne.
    def visitCmdRetorne(self, ctx:LangAlgParser.CmdRetorneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#selecao.
    def visitSelecao(self, ctx:LangAlgParser.SelecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#item_selecao.
    def visitItem_selecao(self, ctx:LangAlgParser.Item_selecaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#constantes.
    def visitConstantes(self, ctx:LangAlgParser.ConstantesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#numero_intervalo.
    def visitNumero_intervalo(self, ctx:LangAlgParser.Numero_intervaloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#op_unario.
    def visitOp_unario(self, ctx:LangAlgParser.Op_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#exp_aritmetica.
    def visitExp_aritmetica(self, ctx:LangAlgParser.Exp_aritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#termo.
    def visitTermo(self, ctx:LangAlgParser.TermoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#fator.
    def visitFator(self, ctx:LangAlgParser.FatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#op1.
    def visitOp1(self, ctx:LangAlgParser.Op1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#op2.
    def visitOp2(self, ctx:LangAlgParser.Op2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#op3.
    def visitOp3(self, ctx:LangAlgParser.Op3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#parcela.
    def visitParcela(self, ctx:LangAlgParser.ParcelaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#parcela_unario.
    def visitParcela_unario(self, ctx:LangAlgParser.Parcela_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#parcela_nao_unario.
    def visitParcela_nao_unario(self, ctx:LangAlgParser.Parcela_nao_unarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#exp_relacional.
    def visitExp_relacional(self, ctx:LangAlgParser.Exp_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#op_relacional.
    def visitOp_relacional(self, ctx:LangAlgParser.Op_relacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#expressao.
    def visitExpressao(self, ctx:LangAlgParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#termo_logico.
    def visitTermo_logico(self, ctx:LangAlgParser.Termo_logicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#fator_logico.
    def visitFator_logico(self, ctx:LangAlgParser.Fator_logicoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#parcela_logica.
    def visitParcela_logica(self, ctx:LangAlgParser.Parcela_logicaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#op_logico_1.
    def visitOp_logico_1(self, ctx:LangAlgParser.Op_logico_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangAlgParser#op_logico_2.
    def visitOp_logico_2(self, ctx:LangAlgParser.Op_logico_2Context):
        return self.visitChildren(ctx)



del LangAlgParser