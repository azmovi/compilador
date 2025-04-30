from os import path

from compilador.exceptions import InvalidPath


def validate_input_file(input_file: str) -> str:
    """Validar se arquivo de entrada existe"""
    if not path.exists(input_file):
        raise InvalidPath(f'wrong file path :{input_file}')
    return input_file


def get_file_content(file_path: str) -> str:
    """Abre um arquivo e retorna seu conteúdo"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
