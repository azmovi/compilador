from antlr4 import FileStream, Token

from compilador.my_token import MyToken
from compilador.parser.LangAlgLexer import LangAlgLexer


def run_lexical_analysis(input_file: str, output_file: str) -> None:
    """Cria o arquivo de output do analisador léxico"""
    token_list = create_token_list(get_lexer(input_file))
    create_output_file(token_list, output_file)


def create_output_file(token_list: list[MyToken], output_path: str):
    """Cria e escreve no arquivo de output"""
    with open(output_path, 'w', encoding='utf-8') as f:
        for token in token_list:
            f.write(str(token) + '\n')


def get_lexer(input_file: str) -> LangAlgLexer:
    """Retorna o objeto léxico da Linguagem Algorítmica"""
    file_stram = FileStream(fileName=input_file, encoding='utf-8')
    return LangAlgLexer(file_stram)


def create_token_list(lexer: LangAlgLexer) -> list[MyToken]:
    """Analisa um objeto léxico retorna uma lista de tokens."""
    token_list = []
    while (token := lexer.nextToken()).type != Token.EOF:
        my_token = MyToken(token.text, token.type, token.line)
        token_list.append(my_token)

        if not my_token.is_valid:
            return token_list
    return token_list
