from dataclasses import dataclass
from enum import Enum

class TipoToken(Enum):
    pass

class TokenIndependente(TipoToken):
    DOIS_PONTOS = ':'
    ABREPAR = '('
    FECHAPAR = ')'
    ABRECOL = '['
    FECHACOL = ']'
    VIRGULA = ','
    PONTO = '.'
    MAIS = '+'
    MENOS = '-'
    MULTIPLICACAO = '*'
    DIVISAO = '/'
    MOD = '%'

class TokenReservado(TipoToken):
    ALGORITMO = 'algoritmo'
    FIM_ALGORITMO = 'fim_algoritmo'
    DECLARE = 'declare'
    TIPO = 'tipo'
    VAR = 'var'
    CONSTANTE = 'constante'
    REGISTRO = 'registro'
    FIM_REGISTRO = 'fim_registro'
    INTEIRO = 'inteiro'
    REAL = 'real'
    LITERAL = 'literal'
    LOGICO = 'logico'
    FALSO = 'falso'
    VERDADEIRO = 'verdadeiro'
    E = 'e'
    OU = 'ou'
    NAO = 'nao'
    SE = 'se'
    SENAO = 'senao'
    ENTAO = 'entao'
    FIM_SE = 'fim_se'
    CASO = 'caso'
    SEJA = 'seja'
    FIM_CASO = 'fim_caso'
    ENQUANTO = 'enquanto'
    FIM_ENQUANTO = 'fim_enquanto'
    PARA = 'para'
    FIM_PARA = 'fim_para'
    FACA = 'faca'
    ATE = 'ate'
    PROCEDIMENTO = 'procedimento'
    FIM_PROCEDIMENTO = 'fim_procedimento'
    FUNCAO = 'funcao'
    FIM_FUNCAO = 'fim_funcao'
    RETORNE = 'retorne'
    LEIA = 'leia'
    ESCREVA = 'escreva'

class TokenRelacional(TipoToken):
    pass

class TokenComparativo(TipoToken):
    IGUAL = '='
    DIFERENCA = '<>'
    MAIOR = '>'
    MENOR = '<'
    MAIOR_IGUAL = '>='
    MENOR_IGUAL = '<='


TOKEN_INDEPENDENTE = {token.value: token for token in TokenIndependente}
TOKEN_COMPARATIVO = {token.value: token for token in TokenComparativo}

@dataclass
class Token:
    tipo: TipoToken
    lexema: str

    def __repr__(self) -> str:
        return f'<{repr(self.tipo.value)}, {repr(self.lexema)}>'
