# Generated from ./LangAlg.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,68,296,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,5,1,77,8,1,10,1,12,1,80,9,1,
        1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,
        3,5,98,8,5,1,6,1,6,1,6,1,6,3,6,104,8,6,1,6,3,6,107,8,6,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,3,7,117,8,7,1,7,3,7,120,8,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,8,1,8,1,8,5,8,131,8,8,10,8,12,8,134,9,8,1,9,1,9,1,9,
        1,9,1,10,5,10,141,8,10,10,10,12,10,144,9,10,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,3,11,155,8,11,1,12,1,12,1,12,1,12,1,12,
        1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,5,14,170,8,14,10,14,12,14,
        173,9,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,3,16,
        185,8,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,195,8,17,1,
        17,1,17,1,18,4,18,200,8,18,11,18,12,18,201,1,19,1,19,1,19,1,19,1,
        20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,3,23,229,8,23,1,23,3,23,232,
        8,23,1,24,1,24,1,24,1,25,1,25,3,25,239,8,25,1,26,1,26,1,26,5,26,
        244,8,26,10,26,12,26,247,9,26,1,27,1,27,1,27,5,27,252,8,27,10,27,
        12,27,255,9,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,264,8,28,
        1,29,1,29,1,29,5,29,269,8,29,10,29,12,29,272,9,29,1,30,1,30,1,30,
        5,30,277,8,30,10,30,12,30,280,9,30,1,31,3,31,283,8,31,1,31,1,31,
        1,31,3,31,288,8,31,1,32,1,32,1,32,1,32,1,33,1,33,1,33,0,0,34,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,0,5,1,0,9,12,2,0,13,14,61,62,1,0,45,46,
        1,0,47,49,1,0,39,44,296,0,68,1,0,0,0,2,78,1,0,0,0,4,81,1,0,0,0,6,
        86,1,0,0,0,8,88,1,0,0,0,10,97,1,0,0,0,12,99,1,0,0,0,14,112,1,0,0,
        0,16,127,1,0,0,0,18,135,1,0,0,0,20,142,1,0,0,0,22,154,1,0,0,0,24,
        156,1,0,0,0,26,161,1,0,0,0,28,166,1,0,0,0,30,174,1,0,0,0,32,178,
        1,0,0,0,34,188,1,0,0,0,36,199,1,0,0,0,38,203,1,0,0,0,40,207,1,0,
        0,0,42,209,1,0,0,0,44,215,1,0,0,0,46,225,1,0,0,0,48,233,1,0,0,0,
        50,238,1,0,0,0,52,240,1,0,0,0,54,248,1,0,0,0,56,263,1,0,0,0,58,265,
        1,0,0,0,60,273,1,0,0,0,62,287,1,0,0,0,64,289,1,0,0,0,66,293,1,0,
        0,0,68,69,5,1,0,0,69,70,3,2,1,0,70,71,3,20,10,0,71,72,5,2,0,0,72,
        1,1,0,0,0,73,77,3,4,2,0,74,77,3,8,4,0,75,77,3,10,5,0,76,73,1,0,0,
        0,76,74,1,0,0,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,
        1,0,0,0,79,3,1,0,0,0,80,78,1,0,0,0,81,82,5,3,0,0,82,83,5,64,0,0,
        83,84,5,56,0,0,84,85,3,6,3,0,85,5,1,0,0,0,86,87,7,0,0,0,87,7,1,0,
        0,0,88,89,5,6,0,0,89,90,5,64,0,0,90,91,5,56,0,0,91,92,3,6,3,0,92,
        93,5,39,0,0,93,94,3,50,25,0,94,9,1,0,0,0,95,98,3,12,6,0,96,98,3,
        14,7,0,97,95,1,0,0,0,97,96,1,0,0,0,98,11,1,0,0,0,99,100,5,31,0,0,
        100,106,5,64,0,0,101,103,5,52,0,0,102,104,3,16,8,0,103,102,1,0,0,
        0,103,104,1,0,0,0,104,105,1,0,0,0,105,107,5,53,0,0,106,101,1,0,0,
        0,106,107,1,0,0,0,107,108,1,0,0,0,108,109,3,2,1,0,109,110,3,20,10,
        0,110,111,5,32,0,0,111,13,1,0,0,0,112,113,5,33,0,0,113,119,5,64,
        0,0,114,116,5,52,0,0,115,117,3,16,8,0,116,115,1,0,0,0,116,117,1,
        0,0,0,117,118,1,0,0,0,118,120,5,53,0,0,119,114,1,0,0,0,119,120,1,
        0,0,0,120,121,1,0,0,0,121,122,5,56,0,0,122,123,3,6,3,0,123,124,3,
        2,1,0,124,125,3,20,10,0,125,126,5,34,0,0,126,15,1,0,0,0,127,132,
        3,18,9,0,128,129,5,57,0,0,129,131,3,18,9,0,130,128,1,0,0,0,131,134,
        1,0,0,0,132,130,1,0,0,0,132,133,1,0,0,0,133,17,1,0,0,0,134,132,1,
        0,0,0,135,136,5,64,0,0,136,137,5,56,0,0,137,138,3,6,3,0,138,19,1,
        0,0,0,139,141,3,22,11,0,140,139,1,0,0,0,141,144,1,0,0,0,142,140,
        1,0,0,0,142,143,1,0,0,0,143,21,1,0,0,0,144,142,1,0,0,0,145,155,3,
        24,12,0,146,155,3,26,13,0,147,155,3,30,15,0,148,155,3,32,16,0,149,
        155,3,34,17,0,150,155,3,42,21,0,151,155,3,44,22,0,152,155,3,46,23,
        0,153,155,3,48,24,0,154,145,1,0,0,0,154,146,1,0,0,0,154,147,1,0,
        0,0,154,148,1,0,0,0,154,149,1,0,0,0,154,150,1,0,0,0,154,151,1,0,
        0,0,154,152,1,0,0,0,154,153,1,0,0,0,155,23,1,0,0,0,156,157,5,36,
        0,0,157,158,5,52,0,0,158,159,5,64,0,0,159,160,5,53,0,0,160,25,1,
        0,0,0,161,162,5,37,0,0,162,163,5,52,0,0,163,164,3,28,14,0,164,165,
        5,53,0,0,165,27,1,0,0,0,166,171,3,50,25,0,167,168,5,57,0,0,168,170,
        3,50,25,0,169,167,1,0,0,0,170,173,1,0,0,0,171,169,1,0,0,0,171,172,
        1,0,0,0,172,29,1,0,0,0,173,171,1,0,0,0,174,175,5,64,0,0,175,176,
        5,38,0,0,176,177,3,50,25,0,177,31,1,0,0,0,178,179,5,18,0,0,179,180,
        3,58,29,0,180,181,5,20,0,0,181,184,3,20,10,0,182,183,5,19,0,0,183,
        185,3,20,10,0,184,182,1,0,0,0,184,185,1,0,0,0,185,186,1,0,0,0,186,
        187,5,21,0,0,187,33,1,0,0,0,188,189,5,22,0,0,189,190,3,50,25,0,190,
        191,5,23,0,0,191,194,3,36,18,0,192,193,5,19,0,0,193,195,3,20,10,
        0,194,192,1,0,0,0,194,195,1,0,0,0,195,196,1,0,0,0,196,197,5,24,0,
        0,197,35,1,0,0,0,198,200,3,38,19,0,199,198,1,0,0,0,200,201,1,0,0,
        0,201,199,1,0,0,0,201,202,1,0,0,0,202,37,1,0,0,0,203,204,3,40,20,
        0,204,205,5,56,0,0,205,206,3,20,10,0,206,39,1,0,0,0,207,208,7,1,
        0,0,208,41,1,0,0,0,209,210,5,25,0,0,210,211,3,58,29,0,211,212,5,
        29,0,0,212,213,3,20,10,0,213,214,5,26,0,0,214,43,1,0,0,0,215,216,
        5,27,0,0,216,217,5,64,0,0,217,218,5,38,0,0,218,219,3,50,25,0,219,
        220,5,30,0,0,220,221,3,50,25,0,221,222,5,29,0,0,222,223,3,20,10,
        0,223,224,5,28,0,0,224,45,1,0,0,0,225,231,5,64,0,0,226,228,5,52,
        0,0,227,229,3,28,14,0,228,227,1,0,0,0,228,229,1,0,0,0,229,230,1,
        0,0,0,230,232,5,53,0,0,231,226,1,0,0,0,231,232,1,0,0,0,232,47,1,
        0,0,0,233,234,5,35,0,0,234,235,3,50,25,0,235,49,1,0,0,0,236,239,
        3,52,26,0,237,239,3,58,29,0,238,236,1,0,0,0,238,237,1,0,0,0,239,
        51,1,0,0,0,240,245,3,54,27,0,241,242,7,2,0,0,242,244,3,54,27,0,243,
        241,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,1,0,0,0,246,
        53,1,0,0,0,247,245,1,0,0,0,248,253,3,56,28,0,249,250,7,3,0,0,250,
        252,3,56,28,0,251,249,1,0,0,0,252,255,1,0,0,0,253,251,1,0,0,0,253,
        254,1,0,0,0,254,55,1,0,0,0,255,253,1,0,0,0,256,264,5,62,0,0,257,
        264,5,63,0,0,258,264,5,64,0,0,259,260,5,52,0,0,260,261,3,52,26,0,
        261,262,5,53,0,0,262,264,1,0,0,0,263,256,1,0,0,0,263,257,1,0,0,0,
        263,258,1,0,0,0,263,259,1,0,0,0,264,57,1,0,0,0,265,270,3,60,30,0,
        266,267,5,16,0,0,267,269,3,60,30,0,268,266,1,0,0,0,269,272,1,0,0,
        0,270,268,1,0,0,0,270,271,1,0,0,0,271,59,1,0,0,0,272,270,1,0,0,0,
        273,278,3,62,31,0,274,275,5,15,0,0,275,277,3,62,31,0,276,274,1,0,
        0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,279,1,0,0,0,279,61,1,0,0,
        0,280,278,1,0,0,0,281,283,5,17,0,0,282,281,1,0,0,0,282,283,1,0,0,
        0,283,284,1,0,0,0,284,288,3,64,32,0,285,288,5,14,0,0,286,288,5,13,
        0,0,287,282,1,0,0,0,287,285,1,0,0,0,287,286,1,0,0,0,288,63,1,0,0,
        0,289,290,3,52,26,0,290,291,3,66,33,0,291,292,3,52,26,0,292,65,1,
        0,0,0,293,294,7,4,0,0,294,67,1,0,0,0,24,76,78,97,103,106,116,119,
        132,142,154,171,184,194,201,228,231,238,245,253,263,270,278,282,
        287
    ]

class LangAlgParser ( Parser ):

    grammarFileName = "LangAlg.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'algoritmo'", "'fim_algoritmo'", "'declare'", 
                     "'tipo'", "'var'", "'constante'", "'registro'", "'fim_registro'", 
                     "'inteiro'", "'real'", "'literal'", "'logico'", "'falso'", 
                     "'verdadeiro'", "'e'", "'ou'", "'nao'", "'se'", "'senao'", 
                     "'entao'", "'fim_se'", "'caso'", "'seja'", "'fim_caso'", 
                     "'enquanto'", "'fim_enquanto'", "'para'", "'fim_para'", 
                     "'faca'", "'ate'", "'procedimento'", "'fim_procedimento'", 
                     "'funcao'", "'fim_funcao'", "'retorne'", "'leia'", 
                     "'escreva'", "'<-'", "'='", "'<>'", "'>'", "'<'", "'>='", 
                     "'<='", "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", "'&'", 
                     "'('", "')'", "'['", "']'", "':'", "','", "'..'", "'.'" ]

    symbolicNames = [ "<INVALID>", "ALGORITMO", "FIM_ALGORITMO", "DECLARE", 
                      "TIPO", "VAR", "CONSTANTE", "REGISTRO", "FIM_REGISTRO", 
                      "INTEIRO", "REAL", "LITERAL", "LOGICO", "FALSO", "VERDADEIRO", 
                      "E", "OU", "NAO", "SE", "SENAO", "ENTAO", "FIM_SE", 
                      "CASO", "SEJA", "FIM_CASO", "ENQUANTO", "FIM_ENQUANTO", 
                      "PARA", "FIM_PARA", "FACA", "ATE", "PROCEDIMENTO", 
                      "FIM_PROCEDIMENTO", "FUNCAO", "FIM_FUNCAO", "RETORNE", 
                      "LEIA", "ESCREVA", "ATRIBUICAO", "IGUAL", "DIFERENTE", 
                      "MAIOR", "MENOR", "MAIOR_IGUAL", "MENOR_IGUAL", "MAIS", 
                      "MENOS", "MULTIPLICACAO", "DIVISAO", "MOD", "PONTEIRO", 
                      "ENDERECO", "ABREPAR", "FECHAPAR", "ABRECOL", "FECHACOL", 
                      "DOIS_PONTOS", "VIRGULA", "PONTO_PONTO", "PONTO", 
                      "CADEIA_NAO_FECHADA", "CADEIA", "NUM_INT", "NUM_REAL", 
                      "IDENT", "COMENTARIO_FECHADO", "COMENTARIO_NAO_FECHADO", 
                      "WS", "ERR" ]

    RULE_programa = 0
    RULE_declaracoes = 1
    RULE_declaracao_var = 2
    RULE_tipo = 3
    RULE_declaracao_const = 4
    RULE_declaracao_subrotina = 5
    RULE_procedimento = 6
    RULE_funcao = 7
    RULE_parametros = 8
    RULE_parametro = 9
    RULE_comandos = 10
    RULE_comando = 11
    RULE_leitura = 12
    RULE_escrita = 13
    RULE_listaExpressao = 14
    RULE_atribuicao = 15
    RULE_se = 16
    RULE_caso = 17
    RULE_seletores = 18
    RULE_seletor = 19
    RULE_valor_constante = 20
    RULE_enquanto = 21
    RULE_para = 22
    RULE_chamadaProcedimento = 23
    RULE_retorne = 24
    RULE_expressao = 25
    RULE_expressao_aritmetica = 26
    RULE_termo_aritmetico = 27
    RULE_fator_aritmetico = 28
    RULE_expressao_logica = 29
    RULE_termo_logico = 30
    RULE_fator_logico = 31
    RULE_relacional = 32
    RULE_operador_relacional = 33

    ruleNames =  [ "programa", "declaracoes", "declaracao_var", "tipo", 
                   "declaracao_const", "declaracao_subrotina", "procedimento", 
                   "funcao", "parametros", "parametro", "comandos", "comando", 
                   "leitura", "escrita", "listaExpressao", "atribuicao", 
                   "se", "caso", "seletores", "seletor", "valor_constante", 
                   "enquanto", "para", "chamadaProcedimento", "retorne", 
                   "expressao", "expressao_aritmetica", "termo_aritmetico", 
                   "fator_aritmetico", "expressao_logica", "termo_logico", 
                   "fator_logico", "relacional", "operador_relacional" ]

    EOF = Token.EOF
    ALGORITMO=1
    FIM_ALGORITMO=2
    DECLARE=3
    TIPO=4
    VAR=5
    CONSTANTE=6
    REGISTRO=7
    FIM_REGISTRO=8
    INTEIRO=9
    REAL=10
    LITERAL=11
    LOGICO=12
    FALSO=13
    VERDADEIRO=14
    E=15
    OU=16
    NAO=17
    SE=18
    SENAO=19
    ENTAO=20
    FIM_SE=21
    CASO=22
    SEJA=23
    FIM_CASO=24
    ENQUANTO=25
    FIM_ENQUANTO=26
    PARA=27
    FIM_PARA=28
    FACA=29
    ATE=30
    PROCEDIMENTO=31
    FIM_PROCEDIMENTO=32
    FUNCAO=33
    FIM_FUNCAO=34
    RETORNE=35
    LEIA=36
    ESCREVA=37
    ATRIBUICAO=38
    IGUAL=39
    DIFERENTE=40
    MAIOR=41
    MENOR=42
    MAIOR_IGUAL=43
    MENOR_IGUAL=44
    MAIS=45
    MENOS=46
    MULTIPLICACAO=47
    DIVISAO=48
    MOD=49
    PONTEIRO=50
    ENDERECO=51
    ABREPAR=52
    FECHAPAR=53
    ABRECOL=54
    FECHACOL=55
    DOIS_PONTOS=56
    VIRGULA=57
    PONTO_PONTO=58
    PONTO=59
    CADEIA_NAO_FECHADA=60
    CADEIA=61
    NUM_INT=62
    NUM_REAL=63
    IDENT=64
    COMENTARIO_FECHADO=65
    COMENTARIO_NAO_FECHADO=66
    WS=67
    ERR=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALGORITMO(self):
            return self.getToken(LangAlgParser.ALGORITMO, 0)

        def declaracoes(self):
            return self.getTypedRuleContext(LangAlgParser.DeclaracoesContext,0)


        def comandos(self):
            return self.getTypedRuleContext(LangAlgParser.ComandosContext,0)


        def FIM_ALGORITMO(self):
            return self.getToken(LangAlgParser.FIM_ALGORITMO, 0)

        def getRuleIndex(self):
            return LangAlgParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = LangAlgParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(LangAlgParser.ALGORITMO)
            self.state = 69
            self.declaracoes()
            self.state = 70
            self.comandos()
            self.state = 71
            self.match(LangAlgParser.FIM_ALGORITMO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.Declaracao_varContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.Declaracao_varContext,i)


        def declaracao_const(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.Declaracao_constContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.Declaracao_constContext,i)


        def declaracao_subrotina(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.Declaracao_subrotinaContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.Declaracao_subrotinaContext,i)


        def getRuleIndex(self):
            return LangAlgParser.RULE_declaracoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes" ):
                listener.enterDeclaracoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes" ):
                listener.exitDeclaracoes(self)




    def declaracoes(self):

        localctx = LangAlgParser.DeclaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 10737418312) != 0):
                self.state = 76
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 73
                    self.declaracao_var()
                    pass
                elif token in [6]:
                    self.state = 74
                    self.declaracao_const()
                    pass
                elif token in [31, 33]:
                    self.state = 75
                    self.declaracao_subrotina()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARE(self):
            return self.getToken(LangAlgParser.DECLARE, 0)

        def IDENT(self):
            return self.getToken(LangAlgParser.IDENT, 0)

        def DOIS_PONTOS(self):
            return self.getToken(LangAlgParser.DOIS_PONTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(LangAlgParser.TipoContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_declaracao_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_var" ):
                listener.enterDeclaracao_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_var" ):
                listener.exitDeclaracao_var(self)




    def declaracao_var(self):

        localctx = LangAlgParser.Declaracao_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaracao_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(LangAlgParser.DECLARE)
            self.state = 82
            self.match(LangAlgParser.IDENT)
            self.state = 83
            self.match(LangAlgParser.DOIS_PONTOS)
            self.state = 84
            self.tipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEIRO(self):
            return self.getToken(LangAlgParser.INTEIRO, 0)

        def REAL(self):
            return self.getToken(LangAlgParser.REAL, 0)

        def LITERAL(self):
            return self.getToken(LangAlgParser.LITERAL, 0)

        def LOGICO(self):
            return self.getToken(LangAlgParser.LOGICO, 0)

        def getRuleIndex(self):
            return LangAlgParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = LangAlgParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7680) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTANTE(self):
            return self.getToken(LangAlgParser.CONSTANTE, 0)

        def IDENT(self):
            return self.getToken(LangAlgParser.IDENT, 0)

        def DOIS_PONTOS(self):
            return self.getToken(LangAlgParser.DOIS_PONTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(LangAlgParser.TipoContext,0)


        def IGUAL(self):
            return self.getToken(LangAlgParser.IGUAL, 0)

        def expressao(self):
            return self.getTypedRuleContext(LangAlgParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_declaracao_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_const" ):
                listener.enterDeclaracao_const(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_const" ):
                listener.exitDeclaracao_const(self)




    def declaracao_const(self):

        localctx = LangAlgParser.Declaracao_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracao_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(LangAlgParser.CONSTANTE)
            self.state = 89
            self.match(LangAlgParser.IDENT)
            self.state = 90
            self.match(LangAlgParser.DOIS_PONTOS)
            self.state = 91
            self.tipo()
            self.state = 92
            self.match(LangAlgParser.IGUAL)
            self.state = 93
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_subrotinaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def procedimento(self):
            return self.getTypedRuleContext(LangAlgParser.ProcedimentoContext,0)


        def funcao(self):
            return self.getTypedRuleContext(LangAlgParser.FuncaoContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_declaracao_subrotina

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_subrotina" ):
                listener.enterDeclaracao_subrotina(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_subrotina" ):
                listener.exitDeclaracao_subrotina(self)




    def declaracao_subrotina(self):

        localctx = LangAlgParser.Declaracao_subrotinaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracao_subrotina)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.procedimento()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.funcao()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProcedimentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDIMENTO(self):
            return self.getToken(LangAlgParser.PROCEDIMENTO, 0)

        def IDENT(self):
            return self.getToken(LangAlgParser.IDENT, 0)

        def declaracoes(self):
            return self.getTypedRuleContext(LangAlgParser.DeclaracoesContext,0)


        def comandos(self):
            return self.getTypedRuleContext(LangAlgParser.ComandosContext,0)


        def FIM_PROCEDIMENTO(self):
            return self.getToken(LangAlgParser.FIM_PROCEDIMENTO, 0)

        def ABREPAR(self):
            return self.getToken(LangAlgParser.ABREPAR, 0)

        def FECHAPAR(self):
            return self.getToken(LangAlgParser.FECHAPAR, 0)

        def parametros(self):
            return self.getTypedRuleContext(LangAlgParser.ParametrosContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_procedimento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProcedimento" ):
                listener.enterProcedimento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProcedimento" ):
                listener.exitProcedimento(self)




    def procedimento(self):

        localctx = LangAlgParser.ProcedimentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_procedimento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(LangAlgParser.PROCEDIMENTO)
            self.state = 100
            self.match(LangAlgParser.IDENT)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 101
                self.match(LangAlgParser.ABREPAR)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==64:
                    self.state = 102
                    self.parametros()


                self.state = 105
                self.match(LangAlgParser.FECHAPAR)


            self.state = 108
            self.declaracoes()
            self.state = 109
            self.comandos()
            self.state = 110
            self.match(LangAlgParser.FIM_PROCEDIMENTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCAO(self):
            return self.getToken(LangAlgParser.FUNCAO, 0)

        def IDENT(self):
            return self.getToken(LangAlgParser.IDENT, 0)

        def DOIS_PONTOS(self):
            return self.getToken(LangAlgParser.DOIS_PONTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(LangAlgParser.TipoContext,0)


        def declaracoes(self):
            return self.getTypedRuleContext(LangAlgParser.DeclaracoesContext,0)


        def comandos(self):
            return self.getTypedRuleContext(LangAlgParser.ComandosContext,0)


        def FIM_FUNCAO(self):
            return self.getToken(LangAlgParser.FIM_FUNCAO, 0)

        def ABREPAR(self):
            return self.getToken(LangAlgParser.ABREPAR, 0)

        def FECHAPAR(self):
            return self.getToken(LangAlgParser.FECHAPAR, 0)

        def parametros(self):
            return self.getTypedRuleContext(LangAlgParser.ParametrosContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_funcao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncao" ):
                listener.enterFuncao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncao" ):
                listener.exitFuncao(self)




    def funcao(self):

        localctx = LangAlgParser.FuncaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(LangAlgParser.FUNCAO)
            self.state = 113
            self.match(LangAlgParser.IDENT)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 114
                self.match(LangAlgParser.ABREPAR)
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==64:
                    self.state = 115
                    self.parametros()


                self.state = 118
                self.match(LangAlgParser.FECHAPAR)


            self.state = 121
            self.match(LangAlgParser.DOIS_PONTOS)
            self.state = 122
            self.tipo()
            self.state = 123
            self.declaracoes()
            self.state = 124
            self.comandos()
            self.state = 125
            self.match(LangAlgParser.FIM_FUNCAO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.ParametroContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.ParametroContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(LangAlgParser.VIRGULA)
            else:
                return self.getToken(LangAlgParser.VIRGULA, i)

        def getRuleIndex(self):
            return LangAlgParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = LangAlgParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.parametro()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 128
                self.match(LangAlgParser.VIRGULA)
                self.state = 129
                self.parametro()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(LangAlgParser.IDENT, 0)

        def DOIS_PONTOS(self):
            return self.getToken(LangAlgParser.DOIS_PONTOS, 0)

        def tipo(self):
            return self.getTypedRuleContext(LangAlgParser.TipoContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)




    def parametro(self):

        localctx = LangAlgParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parametro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(LangAlgParser.IDENT)
            self.state = 136
            self.match(LangAlgParser.DOIS_PONTOS)
            self.state = 137
            self.tipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.ComandoContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.ComandoContext,i)


        def getRuleIndex(self):
            return LangAlgParser.RULE_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandos" ):
                listener.enterComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandos" ):
                listener.exitComandos(self)




    def comandos(self):

        localctx = LangAlgParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comandos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 18)) & ~0x3f) == 0 and ((1 << (_la - 18)) & 70368745095825) != 0):
                self.state = 139
                self.comando()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def leitura(self):
            return self.getTypedRuleContext(LangAlgParser.LeituraContext,0)


        def escrita(self):
            return self.getTypedRuleContext(LangAlgParser.EscritaContext,0)


        def atribuicao(self):
            return self.getTypedRuleContext(LangAlgParser.AtribuicaoContext,0)


        def se(self):
            return self.getTypedRuleContext(LangAlgParser.SeContext,0)


        def caso(self):
            return self.getTypedRuleContext(LangAlgParser.CasoContext,0)


        def enquanto(self):
            return self.getTypedRuleContext(LangAlgParser.EnquantoContext,0)


        def para(self):
            return self.getTypedRuleContext(LangAlgParser.ParaContext,0)


        def chamadaProcedimento(self):
            return self.getTypedRuleContext(LangAlgParser.ChamadaProcedimentoContext,0)


        def retorne(self):
            return self.getTypedRuleContext(LangAlgParser.RetorneContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = LangAlgParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comando)
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.leitura()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.escrita()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.atribuicao()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.se()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 149
                self.caso()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 150
                self.enquanto()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 151
                self.para()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 152
                self.chamadaProcedimento()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 153
                self.retorne()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEIA(self):
            return self.getToken(LangAlgParser.LEIA, 0)

        def ABREPAR(self):
            return self.getToken(LangAlgParser.ABREPAR, 0)

        def IDENT(self):
            return self.getToken(LangAlgParser.IDENT, 0)

        def FECHAPAR(self):
            return self.getToken(LangAlgParser.FECHAPAR, 0)

        def getRuleIndex(self):
            return LangAlgParser.RULE_leitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeitura" ):
                listener.enterLeitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeitura" ):
                listener.exitLeitura(self)




    def leitura(self):

        localctx = LangAlgParser.LeituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_leitura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(LangAlgParser.LEIA)
            self.state = 157
            self.match(LangAlgParser.ABREPAR)
            self.state = 158
            self.match(LangAlgParser.IDENT)
            self.state = 159
            self.match(LangAlgParser.FECHAPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscritaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCREVA(self):
            return self.getToken(LangAlgParser.ESCREVA, 0)

        def ABREPAR(self):
            return self.getToken(LangAlgParser.ABREPAR, 0)

        def listaExpressao(self):
            return self.getTypedRuleContext(LangAlgParser.ListaExpressaoContext,0)


        def FECHAPAR(self):
            return self.getToken(LangAlgParser.FECHAPAR, 0)

        def getRuleIndex(self):
            return LangAlgParser.RULE_escrita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscrita" ):
                listener.enterEscrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscrita" ):
                listener.exitEscrita(self)




    def escrita(self):

        localctx = LangAlgParser.EscritaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_escrita)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(LangAlgParser.ESCREVA)
            self.state = 162
            self.match(LangAlgParser.ABREPAR)
            self.state = 163
            self.listaExpressao()
            self.state = 164
            self.match(LangAlgParser.FECHAPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.ExpressaoContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(LangAlgParser.VIRGULA)
            else:
                return self.getToken(LangAlgParser.VIRGULA, i)

        def getRuleIndex(self):
            return LangAlgParser.RULE_listaExpressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaExpressao" ):
                listener.enterListaExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaExpressao" ):
                listener.exitListaExpressao(self)




    def listaExpressao(self):

        localctx = LangAlgParser.ListaExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listaExpressao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.expressao()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 167
                self.match(LangAlgParser.VIRGULA)
                self.state = 168
                self.expressao()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(LangAlgParser.IDENT, 0)

        def ATRIBUICAO(self):
            return self.getToken(LangAlgParser.ATRIBUICAO, 0)

        def expressao(self):
            return self.getTypedRuleContext(LangAlgParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)




    def atribuicao(self):

        localctx = LangAlgParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(LangAlgParser.IDENT)
            self.state = 175
            self.match(LangAlgParser.ATRIBUICAO)
            self.state = 176
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SE(self):
            return self.getToken(LangAlgParser.SE, 0)

        def expressao_logica(self):
            return self.getTypedRuleContext(LangAlgParser.Expressao_logicaContext,0)


        def ENTAO(self):
            return self.getToken(LangAlgParser.ENTAO, 0)

        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.ComandosContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.ComandosContext,i)


        def FIM_SE(self):
            return self.getToken(LangAlgParser.FIM_SE, 0)

        def SENAO(self):
            return self.getToken(LangAlgParser.SENAO, 0)

        def getRuleIndex(self):
            return LangAlgParser.RULE_se

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSe" ):
                listener.enterSe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSe" ):
                listener.exitSe(self)




    def se(self):

        localctx = LangAlgParser.SeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_se)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.match(LangAlgParser.SE)
            self.state = 179
            self.expressao_logica()
            self.state = 180
            self.match(LangAlgParser.ENTAO)
            self.state = 181
            self.comandos()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 182
                self.match(LangAlgParser.SENAO)
                self.state = 183
                self.comandos()


            self.state = 186
            self.match(LangAlgParser.FIM_SE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASO(self):
            return self.getToken(LangAlgParser.CASO, 0)

        def expressao(self):
            return self.getTypedRuleContext(LangAlgParser.ExpressaoContext,0)


        def SEJA(self):
            return self.getToken(LangAlgParser.SEJA, 0)

        def seletores(self):
            return self.getTypedRuleContext(LangAlgParser.SeletoresContext,0)


        def FIM_CASO(self):
            return self.getToken(LangAlgParser.FIM_CASO, 0)

        def SENAO(self):
            return self.getToken(LangAlgParser.SENAO, 0)

        def comandos(self):
            return self.getTypedRuleContext(LangAlgParser.ComandosContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_caso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaso" ):
                listener.enterCaso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaso" ):
                listener.exitCaso(self)




    def caso(self):

        localctx = LangAlgParser.CasoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_caso)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(LangAlgParser.CASO)
            self.state = 189
            self.expressao()
            self.state = 190
            self.match(LangAlgParser.SEJA)
            self.state = 191
            self.seletores()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 192
                self.match(LangAlgParser.SENAO)
                self.state = 193
                self.comandos()


            self.state = 196
            self.match(LangAlgParser.FIM_CASO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeletoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seletor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.SeletorContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.SeletorContext,i)


        def getRuleIndex(self):
            return LangAlgParser.RULE_seletores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeletores" ):
                listener.enterSeletores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeletores" ):
                listener.exitSeletores(self)




    def seletores(self):

        localctx = LangAlgParser.SeletoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_seletores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 198
                self.seletor()
                self.state = 201 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 6917529027641106432) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeletorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valor_constante(self):
            return self.getTypedRuleContext(LangAlgParser.Valor_constanteContext,0)


        def DOIS_PONTOS(self):
            return self.getToken(LangAlgParser.DOIS_PONTOS, 0)

        def comandos(self):
            return self.getTypedRuleContext(LangAlgParser.ComandosContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_seletor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeletor" ):
                listener.enterSeletor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeletor" ):
                listener.exitSeletor(self)




    def seletor(self):

        localctx = LangAlgParser.SeletorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_seletor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.valor_constante()
            self.state = 204
            self.match(LangAlgParser.DOIS_PONTOS)
            self.state = 205
            self.comandos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Valor_constanteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self):
            return self.getToken(LangAlgParser.NUM_INT, 0)

        def CADEIA(self):
            return self.getToken(LangAlgParser.CADEIA, 0)

        def VERDADEIRO(self):
            return self.getToken(LangAlgParser.VERDADEIRO, 0)

        def FALSO(self):
            return self.getToken(LangAlgParser.FALSO, 0)

        def getRuleIndex(self):
            return LangAlgParser.RULE_valor_constante

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor_constante" ):
                listener.enterValor_constante(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor_constante" ):
                listener.exitValor_constante(self)




    def valor_constante(self):

        localctx = LangAlgParser.Valor_constanteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_valor_constante)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6917529027641106432) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EnquantoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENQUANTO(self):
            return self.getToken(LangAlgParser.ENQUANTO, 0)

        def expressao_logica(self):
            return self.getTypedRuleContext(LangAlgParser.Expressao_logicaContext,0)


        def FACA(self):
            return self.getToken(LangAlgParser.FACA, 0)

        def comandos(self):
            return self.getTypedRuleContext(LangAlgParser.ComandosContext,0)


        def FIM_ENQUANTO(self):
            return self.getToken(LangAlgParser.FIM_ENQUANTO, 0)

        def getRuleIndex(self):
            return LangAlgParser.RULE_enquanto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEnquanto" ):
                listener.enterEnquanto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEnquanto" ):
                listener.exitEnquanto(self)




    def enquanto(self):

        localctx = LangAlgParser.EnquantoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_enquanto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(LangAlgParser.ENQUANTO)
            self.state = 210
            self.expressao_logica()
            self.state = 211
            self.match(LangAlgParser.FACA)
            self.state = 212
            self.comandos()
            self.state = 213
            self.match(LangAlgParser.FIM_ENQUANTO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARA(self):
            return self.getToken(LangAlgParser.PARA, 0)

        def IDENT(self):
            return self.getToken(LangAlgParser.IDENT, 0)

        def ATRIBUICAO(self):
            return self.getToken(LangAlgParser.ATRIBUICAO, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.ExpressaoContext,i)


        def ATE(self):
            return self.getToken(LangAlgParser.ATE, 0)

        def FACA(self):
            return self.getToken(LangAlgParser.FACA, 0)

        def comandos(self):
            return self.getTypedRuleContext(LangAlgParser.ComandosContext,0)


        def FIM_PARA(self):
            return self.getToken(LangAlgParser.FIM_PARA, 0)

        def getRuleIndex(self):
            return LangAlgParser.RULE_para

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPara" ):
                listener.enterPara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPara" ):
                listener.exitPara(self)




    def para(self):

        localctx = LangAlgParser.ParaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_para)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(LangAlgParser.PARA)
            self.state = 216
            self.match(LangAlgParser.IDENT)
            self.state = 217
            self.match(LangAlgParser.ATRIBUICAO)
            self.state = 218
            self.expressao()
            self.state = 219
            self.match(LangAlgParser.ATE)
            self.state = 220
            self.expressao()
            self.state = 221
            self.match(LangAlgParser.FACA)
            self.state = 222
            self.comandos()
            self.state = 223
            self.match(LangAlgParser.FIM_PARA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChamadaProcedimentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(LangAlgParser.IDENT, 0)

        def ABREPAR(self):
            return self.getToken(LangAlgParser.ABREPAR, 0)

        def FECHAPAR(self):
            return self.getToken(LangAlgParser.FECHAPAR, 0)

        def listaExpressao(self):
            return self.getTypedRuleContext(LangAlgParser.ListaExpressaoContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_chamadaProcedimento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChamadaProcedimento" ):
                listener.enterChamadaProcedimento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChamadaProcedimento" ):
                listener.exitChamadaProcedimento(self)




    def chamadaProcedimento(self):

        localctx = LangAlgParser.ChamadaProcedimentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_chamadaProcedimento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(LangAlgParser.IDENT)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 226
                self.match(LangAlgParser.ABREPAR)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 13)) & ~0x3f) == 0 and ((1 << (_la - 13)) & 3941199429763091) != 0):
                    self.state = 227
                    self.listaExpressao()


                self.state = 230
                self.match(LangAlgParser.FECHAPAR)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetorneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNE(self):
            return self.getToken(LangAlgParser.RETORNE, 0)

        def expressao(self):
            return self.getTypedRuleContext(LangAlgParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_retorne

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorne" ):
                listener.enterRetorne(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorne" ):
                listener.exitRetorne(self)




    def retorne(self):

        localctx = LangAlgParser.RetorneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_retorne)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(LangAlgParser.RETORNE)
            self.state = 234
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_aritmetica(self):
            return self.getTypedRuleContext(LangAlgParser.Expressao_aritmeticaContext,0)


        def expressao_logica(self):
            return self.getTypedRuleContext(LangAlgParser.Expressao_logicaContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)




    def expressao(self):

        localctx = LangAlgParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expressao)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.expressao_aritmetica()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.expressao_logica()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expressao_aritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo_aritmetico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.Termo_aritmeticoContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.Termo_aritmeticoContext,i)


        def MAIS(self, i:int=None):
            if i is None:
                return self.getTokens(LangAlgParser.MAIS)
            else:
                return self.getToken(LangAlgParser.MAIS, i)

        def MENOS(self, i:int=None):
            if i is None:
                return self.getTokens(LangAlgParser.MENOS)
            else:
                return self.getToken(LangAlgParser.MENOS, i)

        def getRuleIndex(self):
            return LangAlgParser.RULE_expressao_aritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_aritmetica" ):
                listener.enterExpressao_aritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_aritmetica" ):
                listener.exitExpressao_aritmetica(self)




    def expressao_aritmetica(self):

        localctx = LangAlgParser.Expressao_aritmeticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expressao_aritmetica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.termo_aritmetico()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45 or _la==46:
                self.state = 241
                _la = self._input.LA(1)
                if not(_la==45 or _la==46):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 242
                self.termo_aritmetico()
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Termo_aritmeticoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator_aritmetico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.Fator_aritmeticoContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.Fator_aritmeticoContext,i)


        def MULTIPLICACAO(self, i:int=None):
            if i is None:
                return self.getTokens(LangAlgParser.MULTIPLICACAO)
            else:
                return self.getToken(LangAlgParser.MULTIPLICACAO, i)

        def DIVISAO(self, i:int=None):
            if i is None:
                return self.getTokens(LangAlgParser.DIVISAO)
            else:
                return self.getToken(LangAlgParser.DIVISAO, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(LangAlgParser.MOD)
            else:
                return self.getToken(LangAlgParser.MOD, i)

        def getRuleIndex(self):
            return LangAlgParser.RULE_termo_aritmetico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo_aritmetico" ):
                listener.enterTermo_aritmetico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo_aritmetico" ):
                listener.exitTermo_aritmetico(self)




    def termo_aritmetico(self):

        localctx = LangAlgParser.Termo_aritmeticoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_termo_aritmetico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.fator_aritmetico()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 985162418487296) != 0):
                self.state = 249
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 985162418487296) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 250
                self.fator_aritmetico()
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fator_aritmeticoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self):
            return self.getToken(LangAlgParser.NUM_INT, 0)

        def NUM_REAL(self):
            return self.getToken(LangAlgParser.NUM_REAL, 0)

        def IDENT(self):
            return self.getToken(LangAlgParser.IDENT, 0)

        def ABREPAR(self):
            return self.getToken(LangAlgParser.ABREPAR, 0)

        def expressao_aritmetica(self):
            return self.getTypedRuleContext(LangAlgParser.Expressao_aritmeticaContext,0)


        def FECHAPAR(self):
            return self.getToken(LangAlgParser.FECHAPAR, 0)

        def getRuleIndex(self):
            return LangAlgParser.RULE_fator_aritmetico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator_aritmetico" ):
                listener.enterFator_aritmetico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator_aritmetico" ):
                listener.exitFator_aritmetico(self)




    def fator_aritmetico(self):

        localctx = LangAlgParser.Fator_aritmeticoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_fator_aritmetico)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(LangAlgParser.NUM_INT)
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(LangAlgParser.NUM_REAL)
                pass
            elif token in [64]:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.match(LangAlgParser.IDENT)
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.match(LangAlgParser.ABREPAR)
                self.state = 260
                self.expressao_aritmetica()
                self.state = 261
                self.match(LangAlgParser.FECHAPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expressao_logicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo_logico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.Termo_logicoContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.Termo_logicoContext,i)


        def OU(self, i:int=None):
            if i is None:
                return self.getTokens(LangAlgParser.OU)
            else:
                return self.getToken(LangAlgParser.OU, i)

        def getRuleIndex(self):
            return LangAlgParser.RULE_expressao_logica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_logica" ):
                listener.enterExpressao_logica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_logica" ):
                listener.exitExpressao_logica(self)




    def expressao_logica(self):

        localctx = LangAlgParser.Expressao_logicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expressao_logica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.termo_logico()
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 266
                self.match(LangAlgParser.OU)
                self.state = 267
                self.termo_logico()
                self.state = 272
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Termo_logicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator_logico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.Fator_logicoContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.Fator_logicoContext,i)


        def E(self, i:int=None):
            if i is None:
                return self.getTokens(LangAlgParser.E)
            else:
                return self.getToken(LangAlgParser.E, i)

        def getRuleIndex(self):
            return LangAlgParser.RULE_termo_logico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo_logico" ):
                listener.enterTermo_logico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo_logico" ):
                listener.exitTermo_logico(self)




    def termo_logico(self):

        localctx = LangAlgParser.Termo_logicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_termo_logico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.fator_logico()
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 274
                self.match(LangAlgParser.E)
                self.state = 275
                self.fator_logico()
                self.state = 280
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fator_logicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relacional(self):
            return self.getTypedRuleContext(LangAlgParser.RelacionalContext,0)


        def NAO(self):
            return self.getToken(LangAlgParser.NAO, 0)

        def VERDADEIRO(self):
            return self.getToken(LangAlgParser.VERDADEIRO, 0)

        def FALSO(self):
            return self.getToken(LangAlgParser.FALSO, 0)

        def getRuleIndex(self):
            return LangAlgParser.RULE_fator_logico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator_logico" ):
                listener.enterFator_logico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator_logico" ):
                listener.exitFator_logico(self)




    def fator_logico(self):

        localctx = LangAlgParser.Fator_logicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_fator_logico)
        self._la = 0 # Token type
        try:
            self.state = 287
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 52, 62, 63, 64]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 281
                    self.match(LangAlgParser.NAO)


                self.state = 284
                self.relacional()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.match(LangAlgParser.VERDADEIRO)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 286
                self.match(LangAlgParser.FALSO)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_aritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangAlgParser.Expressao_aritmeticaContext)
            else:
                return self.getTypedRuleContext(LangAlgParser.Expressao_aritmeticaContext,i)


        def operador_relacional(self):
            return self.getTypedRuleContext(LangAlgParser.Operador_relacionalContext,0)


        def getRuleIndex(self):
            return LangAlgParser.RULE_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacional" ):
                listener.enterRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacional" ):
                listener.exitRelacional(self)




    def relacional(self):

        localctx = LangAlgParser.RelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_relacional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.expressao_aritmetica()
            self.state = 290
            self.operador_relacional()
            self.state = 291
            self.expressao_aritmetica()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operador_relacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IGUAL(self):
            return self.getToken(LangAlgParser.IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(LangAlgParser.DIFERENTE, 0)

        def MAIOR(self):
            return self.getToken(LangAlgParser.MAIOR, 0)

        def MENOR(self):
            return self.getToken(LangAlgParser.MENOR, 0)

        def MAIOR_IGUAL(self):
            return self.getToken(LangAlgParser.MAIOR_IGUAL, 0)

        def MENOR_IGUAL(self):
            return self.getToken(LangAlgParser.MENOR_IGUAL, 0)

        def getRuleIndex(self):
            return LangAlgParser.RULE_operador_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperador_relacional" ):
                listener.enterOperador_relacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperador_relacional" ):
                listener.exitOperador_relacional(self)




    def operador_relacional(self):

        localctx = LangAlgParser.Operador_relacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_operador_relacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 34634616274944) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





