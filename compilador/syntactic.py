from antlr4 import CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from antlr4.Token import CommonToken

from compilador.lexical import get_lexer
from compilador.my_token import MyToken
from compilador.parser.LangAlgLexer import LangAlgLexer
from compilador.parser.LangAlgParser import LangAlgParser


class CustomErrorListener(ErrorListener):
    def syntaxError(  # noqa
        self, recognizer, offendingSymbol: CommonToken, line, column, msg, e
    ):
        my_token = MyToken(offendingSymbol.text, offendingSymbol.type, line)
        raise ValueError(my_token)


def get_parser(lexer: LangAlgLexer) -> LangAlgParser:
    """Cria o parser da Linguagem Algorítmica e adicionar um Listener Customizado"""
    token_stream = CommonTokenStream(lexer)
    parser = LangAlgParser(token_stream)
    custom_listener = CustomErrorListener()
    parser.addErrorListener(custom_listener)
    return parser


def run_syntactic_analysis(input_file: str, output_file: str):
    """Tenta rodar a analise sintática e escreve em um arquivo caso falhe"""
    try:
        lexer = get_lexer(input_file)
        parser = get_parser(lexer)
        parser.programa()
    except ValueError as e:
        token = e.args[0]
        syntatic_error = get_syntatic_error(token)
        create_output_file(syntatic_error, output_file)
    finally:
        return


def get_syntatic_error(token: MyToken) -> str:
    """Pegar a mensagem para escrever no arquivo de output"""
    if token.type == -1:
        msg = f'Linha {token.line}: erro sintatico proximo a EOF'
    else:
        msg = f'Linha {token.line}: erro sintatico proximo a {token.text}'
    return msg if token.is_valid else repr(token)


def create_output_file(syntatic_error: str, output_path: str):
    """Cria e escreve no arquivo de output"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(syntatic_error + '\n')
        f.write('Fim da compilacao\n')
