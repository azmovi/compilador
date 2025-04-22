from typing import Iterator

from compilador.schemas import TokenComparativo, TOKEN_INDEPENDENTE, Token, TOKEN_COMPARATIVO
from compilador.utils import arquvi


def get_tokens(file: Iterator[str]) -> list[Token]:
    token_list = []
    for caracter in file:
        print(caracter)
        if not is_invalid_caracter(caracter):
            token_list.append(get_token(file,caracter))

    return token_list

def get_token(file: Iterator[str], caracter: str):
    if tipo := TOKEN_INDEPENDENTE.get(caracter):
        token = Token(tipo, caracter)

    elif tipo := TOKEN_COMPARATIVO.get(caracter):
        next_caracter = next(file)
        if next_caracter == '>':
            token = Token(TokenComparativo.DIFERENCA,'<>')

        token = Token(tipo, caracter)

    else:
        token = None
    return token 
        


def is_invalid_caracter(caraceter: str) -> bool:
    invalid_caracter = {'\n', '\t'}
    return caraceter in invalid_caracter


def main():
    token_list = get_tokens(arquvi)
    print(token_list)

main()
