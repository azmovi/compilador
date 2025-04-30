from antlr4 import CommonTokenStream
from antlr4.Token import CommonToken
from antlr4.error.ErrorListener import ErrorListener
from compilador.lexical import get_lang_alg_lexer
from compilador.parser.LangAlgLexer import LangAlgLexer
from compilador.parser.LangAlgParser import LangAlgParser

from antlr4.error.Errors import IllegalStateException

class CustomErrorListener(ErrorListener):
    erros = {
        'COMENTARIO_NAO_FECHADO': 'comentario nao fechado',
        'CADEIA_NAO_FECHADA': 'cadeia literal nao fechada',
        'ERRO': '- simbolo nao identificado',
    }

    def __init__(self, output_file: str):
        self.output_file = output_file

    def syntaxError(self, recognizer, offendingSymbol: CommonToken, line, column, msg, e):
        with open(self.output_file, 'w', encoding='utf-8') as f:
            try:
                error_msg = self.create_error_message(offendingSymbol)

                if  error_msg ==  '- simbolo nao identificado':
                    f.write(f'Linha {line}: {offendingSymbol.text} {error_msg}\n')
                else:
                    f.write(f'Linha {line}: {error_msg}\n')

            except (IndexError, KeyError):
                f.write(f'Linha {line}: erro sintatico proximo a {offendingSymbol.text}\n')
            except IllegalStateException:
                f.write(f'Linha {line}: erro sintatico proximo a EOF\n')

            finally:
                f.write('Fim da compilacao\n')
                raise Exception


    def create_error_message(self, token: CommonToken):
        if token.type < 0:
            raise IllegalStateException('EOF')

        type_error = LangAlgLexer.ruleNames[token.type] 
        return self.erros[type_error]



def run_syntactic_analysis(input_file: str, output_file: str):
    lang_alg_lexer = get_lang_alg_lexer(input_file)
    token_stream = CommonTokenStream(lang_alg_lexer)
    parser = LangAlgParser(token_stream)

    custom_listener = CustomErrorListener(output_file)
    parser.addErrorListener(custom_listener)

    try:
        parser.programa()
    except Exception:
        return
