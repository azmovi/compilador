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


    # Enter a parse tree produced by LangAlgParser#declaracoes.
    def enterDeclaracoes(self, ctx:LangAlgParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by LangAlgParser#declaracoes.
    def exitDeclaracoes(self, ctx:LangAlgParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by LangAlgParser#decl_local_global.
    def enterDecl_local_global(self, ctx:LangAlgParser.Decl_local_globalContext):
        pass

    # Exit a parse tree produced by LangAlgParser#decl_local_global.
    def exitDecl_local_global(self, ctx:LangAlgParser.Decl_local_globalContext):
        pass


    # Enter a parse tree produced by LangAlgParser#declaracao_local.
    def enterDeclaracao_local(self, ctx:LangAlgParser.Declaracao_localContext):
        pass

    # Exit a parse tree produced by LangAlgParser#declaracao_local.
    def exitDeclaracao_local(self, ctx:LangAlgParser.Declaracao_localContext):
        pass


    # Enter a parse tree produced by LangAlgParser#variavel.
    def enterVariavel(self, ctx:LangAlgParser.VariavelContext):
        pass

    # Exit a parse tree produced by LangAlgParser#variavel.
    def exitVariavel(self, ctx:LangAlgParser.VariavelContext):
        pass


    # Enter a parse tree produced by LangAlgParser#identificador.
    def enterIdentificador(self, ctx:LangAlgParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by LangAlgParser#identificador.
    def exitIdentificador(self, ctx:LangAlgParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by LangAlgParser#dimensao.
    def enterDimensao(self, ctx:LangAlgParser.DimensaoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#dimensao.
    def exitDimensao(self, ctx:LangAlgParser.DimensaoContext):
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


    # Enter a parse tree produced by LangAlgParser#tipo_basico_ident.
    def enterTipo_basico_ident(self, ctx:LangAlgParser.Tipo_basico_identContext):
        pass

    # Exit a parse tree produced by LangAlgParser#tipo_basico_ident.
    def exitTipo_basico_ident(self, ctx:LangAlgParser.Tipo_basico_identContext):
        pass


    # Enter a parse tree produced by LangAlgParser#tipo_estendido.
    def enterTipo_estendido(self, ctx:LangAlgParser.Tipo_estendidoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#tipo_estendido.
    def exitTipo_estendido(self, ctx:LangAlgParser.Tipo_estendidoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#valor_constante.
    def enterValor_constante(self, ctx:LangAlgParser.Valor_constanteContext):
        pass

    # Exit a parse tree produced by LangAlgParser#valor_constante.
    def exitValor_constante(self, ctx:LangAlgParser.Valor_constanteContext):
        pass


    # Enter a parse tree produced by LangAlgParser#registro.
    def enterRegistro(self, ctx:LangAlgParser.RegistroContext):
        pass

    # Exit a parse tree produced by LangAlgParser#registro.
    def exitRegistro(self, ctx:LangAlgParser.RegistroContext):
        pass


    # Enter a parse tree produced by LangAlgParser#declaracao_global.
    def enterDeclaracao_global(self, ctx:LangAlgParser.Declaracao_globalContext):
        pass

    # Exit a parse tree produced by LangAlgParser#declaracao_global.
    def exitDeclaracao_global(self, ctx:LangAlgParser.Declaracao_globalContext):
        pass


    # Enter a parse tree produced by LangAlgParser#parametro.
    def enterParametro(self, ctx:LangAlgParser.ParametroContext):
        pass

    # Exit a parse tree produced by LangAlgParser#parametro.
    def exitParametro(self, ctx:LangAlgParser.ParametroContext):
        pass


    # Enter a parse tree produced by LangAlgParser#parametros.
    def enterParametros(self, ctx:LangAlgParser.ParametrosContext):
        pass

    # Exit a parse tree produced by LangAlgParser#parametros.
    def exitParametros(self, ctx:LangAlgParser.ParametrosContext):
        pass


    # Enter a parse tree produced by LangAlgParser#corpo.
    def enterCorpo(self, ctx:LangAlgParser.CorpoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#corpo.
    def exitCorpo(self, ctx:LangAlgParser.CorpoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#cmd.
    def enterCmd(self, ctx:LangAlgParser.CmdContext):
        pass

    # Exit a parse tree produced by LangAlgParser#cmd.
    def exitCmd(self, ctx:LangAlgParser.CmdContext):
        pass


    # Enter a parse tree produced by LangAlgParser#cmdLeia.
    def enterCmdLeia(self, ctx:LangAlgParser.CmdLeiaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#cmdLeia.
    def exitCmdLeia(self, ctx:LangAlgParser.CmdLeiaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#cmdEscreva.
    def enterCmdEscreva(self, ctx:LangAlgParser.CmdEscrevaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#cmdEscreva.
    def exitCmdEscreva(self, ctx:LangAlgParser.CmdEscrevaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#cmdSe.
    def enterCmdSe(self, ctx:LangAlgParser.CmdSeContext):
        pass

    # Exit a parse tree produced by LangAlgParser#cmdSe.
    def exitCmdSe(self, ctx:LangAlgParser.CmdSeContext):
        pass


    # Enter a parse tree produced by LangAlgParser#cmdCaso.
    def enterCmdCaso(self, ctx:LangAlgParser.CmdCasoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#cmdCaso.
    def exitCmdCaso(self, ctx:LangAlgParser.CmdCasoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#cmdPara.
    def enterCmdPara(self, ctx:LangAlgParser.CmdParaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#cmdPara.
    def exitCmdPara(self, ctx:LangAlgParser.CmdParaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#cmdEnquanto.
    def enterCmdEnquanto(self, ctx:LangAlgParser.CmdEnquantoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#cmdEnquanto.
    def exitCmdEnquanto(self, ctx:LangAlgParser.CmdEnquantoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#cmdFaca.
    def enterCmdFaca(self, ctx:LangAlgParser.CmdFacaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#cmdFaca.
    def exitCmdFaca(self, ctx:LangAlgParser.CmdFacaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#cmdAtribuicao.
    def enterCmdAtribuicao(self, ctx:LangAlgParser.CmdAtribuicaoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#cmdAtribuicao.
    def exitCmdAtribuicao(self, ctx:LangAlgParser.CmdAtribuicaoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#cmdChamada.
    def enterCmdChamada(self, ctx:LangAlgParser.CmdChamadaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#cmdChamada.
    def exitCmdChamada(self, ctx:LangAlgParser.CmdChamadaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#cmdRetorne.
    def enterCmdRetorne(self, ctx:LangAlgParser.CmdRetorneContext):
        pass

    # Exit a parse tree produced by LangAlgParser#cmdRetorne.
    def exitCmdRetorne(self, ctx:LangAlgParser.CmdRetorneContext):
        pass


    # Enter a parse tree produced by LangAlgParser#selecao.
    def enterSelecao(self, ctx:LangAlgParser.SelecaoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#selecao.
    def exitSelecao(self, ctx:LangAlgParser.SelecaoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#item_selecao.
    def enterItem_selecao(self, ctx:LangAlgParser.Item_selecaoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#item_selecao.
    def exitItem_selecao(self, ctx:LangAlgParser.Item_selecaoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#constantes.
    def enterConstantes(self, ctx:LangAlgParser.ConstantesContext):
        pass

    # Exit a parse tree produced by LangAlgParser#constantes.
    def exitConstantes(self, ctx:LangAlgParser.ConstantesContext):
        pass


    # Enter a parse tree produced by LangAlgParser#numero_intervalo.
    def enterNumero_intervalo(self, ctx:LangAlgParser.Numero_intervaloContext):
        pass

    # Exit a parse tree produced by LangAlgParser#numero_intervalo.
    def exitNumero_intervalo(self, ctx:LangAlgParser.Numero_intervaloContext):
        pass


    # Enter a parse tree produced by LangAlgParser#op_unario.
    def enterOp_unario(self, ctx:LangAlgParser.Op_unarioContext):
        pass

    # Exit a parse tree produced by LangAlgParser#op_unario.
    def exitOp_unario(self, ctx:LangAlgParser.Op_unarioContext):
        pass


    # Enter a parse tree produced by LangAlgParser#exp_aritmetica.
    def enterExp_aritmetica(self, ctx:LangAlgParser.Exp_aritmeticaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#exp_aritmetica.
    def exitExp_aritmetica(self, ctx:LangAlgParser.Exp_aritmeticaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#termo.
    def enterTermo(self, ctx:LangAlgParser.TermoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#termo.
    def exitTermo(self, ctx:LangAlgParser.TermoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#fator.
    def enterFator(self, ctx:LangAlgParser.FatorContext):
        pass

    # Exit a parse tree produced by LangAlgParser#fator.
    def exitFator(self, ctx:LangAlgParser.FatorContext):
        pass


    # Enter a parse tree produced by LangAlgParser#op1.
    def enterOp1(self, ctx:LangAlgParser.Op1Context):
        pass

    # Exit a parse tree produced by LangAlgParser#op1.
    def exitOp1(self, ctx:LangAlgParser.Op1Context):
        pass


    # Enter a parse tree produced by LangAlgParser#op2.
    def enterOp2(self, ctx:LangAlgParser.Op2Context):
        pass

    # Exit a parse tree produced by LangAlgParser#op2.
    def exitOp2(self, ctx:LangAlgParser.Op2Context):
        pass


    # Enter a parse tree produced by LangAlgParser#op3.
    def enterOp3(self, ctx:LangAlgParser.Op3Context):
        pass

    # Exit a parse tree produced by LangAlgParser#op3.
    def exitOp3(self, ctx:LangAlgParser.Op3Context):
        pass


    # Enter a parse tree produced by LangAlgParser#parcela.
    def enterParcela(self, ctx:LangAlgParser.ParcelaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#parcela.
    def exitParcela(self, ctx:LangAlgParser.ParcelaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#parcela_unario.
    def enterParcela_unario(self, ctx:LangAlgParser.Parcela_unarioContext):
        pass

    # Exit a parse tree produced by LangAlgParser#parcela_unario.
    def exitParcela_unario(self, ctx:LangAlgParser.Parcela_unarioContext):
        pass


    # Enter a parse tree produced by LangAlgParser#parcela_nao_unario.
    def enterParcela_nao_unario(self, ctx:LangAlgParser.Parcela_nao_unarioContext):
        pass

    # Exit a parse tree produced by LangAlgParser#parcela_nao_unario.
    def exitParcela_nao_unario(self, ctx:LangAlgParser.Parcela_nao_unarioContext):
        pass


    # Enter a parse tree produced by LangAlgParser#exp_relacional.
    def enterExp_relacional(self, ctx:LangAlgParser.Exp_relacionalContext):
        pass

    # Exit a parse tree produced by LangAlgParser#exp_relacional.
    def exitExp_relacional(self, ctx:LangAlgParser.Exp_relacionalContext):
        pass


    # Enter a parse tree produced by LangAlgParser#op_relacional.
    def enterOp_relacional(self, ctx:LangAlgParser.Op_relacionalContext):
        pass

    # Exit a parse tree produced by LangAlgParser#op_relacional.
    def exitOp_relacional(self, ctx:LangAlgParser.Op_relacionalContext):
        pass


    # Enter a parse tree produced by LangAlgParser#expressao.
    def enterExpressao(self, ctx:LangAlgParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#expressao.
    def exitExpressao(self, ctx:LangAlgParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#termo_logico.
    def enterTermo_logico(self, ctx:LangAlgParser.Termo_logicoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#termo_logico.
    def exitTermo_logico(self, ctx:LangAlgParser.Termo_logicoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#fator_logico.
    def enterFator_logico(self, ctx:LangAlgParser.Fator_logicoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#fator_logico.
    def exitFator_logico(self, ctx:LangAlgParser.Fator_logicoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#parcela_logica.
    def enterParcela_logica(self, ctx:LangAlgParser.Parcela_logicaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#parcela_logica.
    def exitParcela_logica(self, ctx:LangAlgParser.Parcela_logicaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#op_logico_1.
    def enterOp_logico_1(self, ctx:LangAlgParser.Op_logico_1Context):
        pass

    # Exit a parse tree produced by LangAlgParser#op_logico_1.
    def exitOp_logico_1(self, ctx:LangAlgParser.Op_logico_1Context):
        pass


    # Enter a parse tree produced by LangAlgParser#op_logico_2.
    def enterOp_logico_2(self, ctx:LangAlgParser.Op_logico_2Context):
        pass

    # Exit a parse tree produced by LangAlgParser#op_logico_2.
    def exitOp_logico_2(self, ctx:LangAlgParser.Op_logico_2Context):
        pass



del LangAlgParser