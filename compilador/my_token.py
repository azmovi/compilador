from antlr4 import Token
from compilador.parser.LangAlgLexer import LangAlgLexer


class MyToken:
    """Classe para representar um token da Linguagem Algorítmica"""

    erros = {
        'COMENTARIO_NAO_FECHADO': 'comentario nao fechado',
        'CADEIA_NAO_FECHADA': 'cadeia literal nao fechada',
        'ERRO': '- simbolo nao identificado',
    }

    def __init__(self, text: str, type: int, line: int) -> None:
        self.text = text
        self.type = type
        self.line = line

    def __repr__(self) -> str:
        if self.is_valid:
            msg = f'<{repr(self.text)},{self.name}>'
        else:
            error_msg = self.erros[self.name]
            if self.name == 'ERRO':
                msg = f'Linha {self.line}: {self.text} {error_msg}'
            else:
                msg = f'Linha {self.line}: {error_msg}'
        return msg

    @property
    def name(self) -> str:
        if self.type == Token.EOF:
            return "EOF"
        elif repr(self.text) in LangAlgLexer.literalNames:
            return repr(self.text)
        else:
            return LangAlgLexer.symbolicNames[self.type]

    @property
    def is_valid(self) -> bool:
        """Verifica os três erros possíveis do léxico"""
        return self.name not in self.erros
