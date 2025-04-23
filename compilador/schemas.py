from dataclasses import dataclass

from antlr4 import Token

from compilador.parser.LangAlg import LangAlg


@dataclass
class MyToken:
    pass


@dataclass
class ValidToken(MyToken):
    tipo: Token
    text: str

    def __repr__(self) -> str:
        try:
            tipo_exp = LangAlg.literalNames[self.tipo]
        except IndexError:
            tipo_exp = LangAlg.symbolicNames[self.tipo]

        return f'<{repr(self.text)},{tipo_exp}>'


@dataclass
class ErrorToken(MyToken):
    linha: int
    error_msg: str
    text: str

    def __repr__(self) -> str:
        if self.error_msg == '- simbolo nao identificado':
            return f'Linha {self.linha}: {self.text} - {self.error_msg}'
        else:
            return f'Linha {self.linha}: {self.error_msg}'
