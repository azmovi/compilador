from os import path

from compilador.constants import PATH
from compilador.exceptions import InvalidPath


def get_file_path(input_file: str, output_file: str) -> tuple[str, str]:
    """Pegar o path completo do arquivo de input e output"""
    input = f'{input_file}'
    output = f'{output_file}'
    if not path.exists(input_file):
        raise InvalidPath(f'wrong file path :{input_file}')
    return input, output


def get_file_content(file_path: str) -> str:
    """Abre um arquivo e retorna seu gerador de caracteres"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
