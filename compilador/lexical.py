from antlr4 import  Token, FileStream
from compilador.parser.LangAlgLexer import LangAlgLexer
from compilador.schemas import ErrorToken, MyToken, ValidToken


def run_lexical_analysis(input_file: str, output_file: str) -> None:
    """Cria o arquivo de output do analisador léxico"""
    lang_alg_lexer = get_lang_alg_lexer(input_file)
    token_list = create_token_list(lang_alg_lexer)
    create_output_file(token_list, output_file)


def create_output_file(token_list: list[MyToken], output_path: str):
    """Cria e escreve no arquivo de output"""
    with open(output_path, 'w', encoding='utf-8') as f:
        for token in token_list:
            f.write(str(token) + '\n')


def get_lang_alg_lexer(input_file: str) -> LangAlgLexer:
    """Retonar o objeto lexico de um arquivo"""
    file_stram = FileStream(fileName=input_file, encoding='utf-8')
    return LangAlgLexer(file_stram)


def create_token_list(lang_alg_lexer: LangAlgLexer) -> list[MyToken]:
    """Analisa um objeto lexico retorna uma lista de tokens."""
    token_list = []
    while (token := lang_alg_lexer.nextToken()).type != Token.EOF:
        if error_msg := get_invalid_token(token):
            my_token = ErrorToken(token.line, error_msg, token.text)
        else:
            my_token = ValidToken(token.type, token.text)

        token_list.append(my_token)

        if isinstance(my_token, ErrorToken):
            return token_list

    return token_list


def get_invalid_token(token) -> str | None:
    """Verifica os três erros possíveis do léxico"""
    erros = {
        'COMENTARIO_NAO_FECHADO': 'comentario nao fechado',
        'CADEIA_NAO_FECHADA': 'cadeia literal nao fechada',
        'ERR': ' - simbolo nao identificado',
    }
    tipo = LangAlgLexer.ruleNames[token.type]
    return erros.get(tipo, None)
