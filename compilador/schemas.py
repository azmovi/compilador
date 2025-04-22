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
