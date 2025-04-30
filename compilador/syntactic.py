from antlr4 import CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from compilador.parser.LangAlg import LangAlg
from compilador.parser.LangAlgParser import LangAlgParser
from compilador.schemas import MyToken


class CustomSyntacticErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        token_text = offendingSymbol.text if offendingSymbol else ''
        error_message = f"Linha {line}: erro sintatico proximo a {token_text}"
        self.errors.append(error_message)

def run_syntactic_analysis(tokens: LangAlg, output_file: str):
    token_stream = CommonTokenStream(tokens)
    parser = LangAlgParser(token_stream)

    # Adicionar o nosso
    __import__('ipdb').set_trace()
    custom_listener = CustomSyntacticErrorListener()
    parser.addErrorListener(custom_listener)

    parser.programa()

