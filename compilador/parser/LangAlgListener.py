# Generated from ./LangAlg.g4 by ANTLR 4.13.2
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


    # Enter a parse tree produced by LangAlgParser#declaracao_var.
    def enterDeclaracao_var(self, ctx:LangAlgParser.Declaracao_varContext):
        pass

    # Exit a parse tree produced by LangAlgParser#declaracao_var.
    def exitDeclaracao_var(self, ctx:LangAlgParser.Declaracao_varContext):
        pass


    # Enter a parse tree produced by LangAlgParser#tipo.
    def enterTipo(self, ctx:LangAlgParser.TipoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#tipo.
    def exitTipo(self, ctx:LangAlgParser.TipoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#declaracao_const.
    def enterDeclaracao_const(self, ctx:LangAlgParser.Declaracao_constContext):
        pass

    # Exit a parse tree produced by LangAlgParser#declaracao_const.
    def exitDeclaracao_const(self, ctx:LangAlgParser.Declaracao_constContext):
        pass


    # Enter a parse tree produced by LangAlgParser#declaracao_subrotina.
    def enterDeclaracao_subrotina(self, ctx:LangAlgParser.Declaracao_subrotinaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#declaracao_subrotina.
    def exitDeclaracao_subrotina(self, ctx:LangAlgParser.Declaracao_subrotinaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#procedimento.
    def enterProcedimento(self, ctx:LangAlgParser.ProcedimentoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#procedimento.
    def exitProcedimento(self, ctx:LangAlgParser.ProcedimentoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#funcao.
    def enterFuncao(self, ctx:LangAlgParser.FuncaoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#funcao.
    def exitFuncao(self, ctx:LangAlgParser.FuncaoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#parametros.
    def enterParametros(self, ctx:LangAlgParser.ParametrosContext):
        pass

    # Exit a parse tree produced by LangAlgParser#parametros.
    def exitParametros(self, ctx:LangAlgParser.ParametrosContext):
        pass


    # Enter a parse tree produced by LangAlgParser#parametro.
    def enterParametro(self, ctx:LangAlgParser.ParametroContext):
        pass

    # Exit a parse tree produced by LangAlgParser#parametro.
    def exitParametro(self, ctx:LangAlgParser.ParametroContext):
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


    # Enter a parse tree produced by LangAlgParser#leitura.
    def enterLeitura(self, ctx:LangAlgParser.LeituraContext):
        pass

    # Exit a parse tree produced by LangAlgParser#leitura.
    def exitLeitura(self, ctx:LangAlgParser.LeituraContext):
        pass


    # Enter a parse tree produced by LangAlgParser#escrita.
    def enterEscrita(self, ctx:LangAlgParser.EscritaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#escrita.
    def exitEscrita(self, ctx:LangAlgParser.EscritaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#listaExpressao.
    def enterListaExpressao(self, ctx:LangAlgParser.ListaExpressaoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#listaExpressao.
    def exitListaExpressao(self, ctx:LangAlgParser.ListaExpressaoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#atribuicao.
    def enterAtribuicao(self, ctx:LangAlgParser.AtribuicaoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#atribuicao.
    def exitAtribuicao(self, ctx:LangAlgParser.AtribuicaoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#se.
    def enterSe(self, ctx:LangAlgParser.SeContext):
        pass

    # Exit a parse tree produced by LangAlgParser#se.
    def exitSe(self, ctx:LangAlgParser.SeContext):
        pass


    # Enter a parse tree produced by LangAlgParser#caso.
    def enterCaso(self, ctx:LangAlgParser.CasoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#caso.
    def exitCaso(self, ctx:LangAlgParser.CasoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#seletores.
    def enterSeletores(self, ctx:LangAlgParser.SeletoresContext):
        pass

    # Exit a parse tree produced by LangAlgParser#seletores.
    def exitSeletores(self, ctx:LangAlgParser.SeletoresContext):
        pass


    # Enter a parse tree produced by LangAlgParser#seletor.
    def enterSeletor(self, ctx:LangAlgParser.SeletorContext):
        pass

    # Exit a parse tree produced by LangAlgParser#seletor.
    def exitSeletor(self, ctx:LangAlgParser.SeletorContext):
        pass


    # Enter a parse tree produced by LangAlgParser#valor_constante.
    def enterValor_constante(self, ctx:LangAlgParser.Valor_constanteContext):
        pass

    # Exit a parse tree produced by LangAlgParser#valor_constante.
    def exitValor_constante(self, ctx:LangAlgParser.Valor_constanteContext):
        pass


    # Enter a parse tree produced by LangAlgParser#enquanto.
    def enterEnquanto(self, ctx:LangAlgParser.EnquantoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#enquanto.
    def exitEnquanto(self, ctx:LangAlgParser.EnquantoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#para.
    def enterPara(self, ctx:LangAlgParser.ParaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#para.
    def exitPara(self, ctx:LangAlgParser.ParaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#chamadaProcedimento.
    def enterChamadaProcedimento(self, ctx:LangAlgParser.ChamadaProcedimentoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#chamadaProcedimento.
    def exitChamadaProcedimento(self, ctx:LangAlgParser.ChamadaProcedimentoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#retorne.
    def enterRetorne(self, ctx:LangAlgParser.RetorneContext):
        pass

    # Exit a parse tree produced by LangAlgParser#retorne.
    def exitRetorne(self, ctx:LangAlgParser.RetorneContext):
        pass


    # Enter a parse tree produced by LangAlgParser#expressao.
    def enterExpressao(self, ctx:LangAlgParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#expressao.
    def exitExpressao(self, ctx:LangAlgParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#expressao_aritmetica.
    def enterExpressao_aritmetica(self, ctx:LangAlgParser.Expressao_aritmeticaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#expressao_aritmetica.
    def exitExpressao_aritmetica(self, ctx:LangAlgParser.Expressao_aritmeticaContext):
        pass


    # Enter a parse tree produced by LangAlgParser#termo_aritmetico.
    def enterTermo_aritmetico(self, ctx:LangAlgParser.Termo_aritmeticoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#termo_aritmetico.
    def exitTermo_aritmetico(self, ctx:LangAlgParser.Termo_aritmeticoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#fator_aritmetico.
    def enterFator_aritmetico(self, ctx:LangAlgParser.Fator_aritmeticoContext):
        pass

    # Exit a parse tree produced by LangAlgParser#fator_aritmetico.
    def exitFator_aritmetico(self, ctx:LangAlgParser.Fator_aritmeticoContext):
        pass


    # Enter a parse tree produced by LangAlgParser#expressao_logica.
    def enterExpressao_logica(self, ctx:LangAlgParser.Expressao_logicaContext):
        pass

    # Exit a parse tree produced by LangAlgParser#expressao_logica.
    def exitExpressao_logica(self, ctx:LangAlgParser.Expressao_logicaContext):
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


    # Enter a parse tree produced by LangAlgParser#relacional.
    def enterRelacional(self, ctx:LangAlgParser.RelacionalContext):
        pass

    # Exit a parse tree produced by LangAlgParser#relacional.
    def exitRelacional(self, ctx:LangAlgParser.RelacionalContext):
        pass


    # Enter a parse tree produced by LangAlgParser#operador_relacional.
    def enterOperador_relacional(self, ctx:LangAlgParser.Operador_relacionalContext):
        pass

    # Exit a parse tree produced by LangAlgParser#operador_relacional.
    def exitOperador_relacional(self, ctx:LangAlgParser.Operador_relacionalContext):
        pass



del LangAlgParser