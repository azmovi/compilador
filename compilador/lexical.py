from antlr4 import InputStream, Token

from compilador.file_reader import get_file_content
from compilador.parser.LangAlg import LangAlg
from compilador.schemas import ErrorToken, MyToken, ValidToken


def create_lexical(input_path: str, output_path: str):
    """Cria o arquivo de output do analisador léxico"""
    file_content = get_file_content(input_path)
    token_list = get_token_list(file_content)
    create_output_file(output_path, token_list)


def create_output_file(output_path: str, token_list: list[MyToken]):
    """Cria e escreve no arquivo de output"""
    with open(output_path, 'w', encoding='utf-8') as f:
        for token in token_list:
            f.write(str(token) + '\n')


def get_token_list(file_content: str) -> list[MyToken]:
    """Analisa o conteúdo de um arquivo fonte e retorna uma lista de tokens."""
    input_stream = InputStream(file_content)
    tokens = LangAlg(input_stream)
    token_list = []

    while (token := tokens.nextToken()).type != Token.EOF:
        if error_msg := is_invalid_token(token):
            my_token = ErrorToken(token.line, error_msg, token.text)
        else:
            my_token = ValidToken(token.type, token.text)

        token_list.append(my_token)

        if isinstance(my_token, ErrorToken):
            return token_list

    return token_list


def is_invalid_token(token) -> str | None:
    """Verifica os três erros possíveis do léxico"""
    erros = {
        'COMENTARIO_NAO_FECHADO': 'comentario nao fechado',
        'CADEIA_NAO_FECHADA': 'cadeia literal nao fechada',
        'ERR': ' - simbolo nao identificado',
    }
    tipo = LangAlg.symbolicNames[token.type]
    return erros.get(tipo, None)
