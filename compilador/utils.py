from os import path
from typing import Iterator
from compilador.constants import PATH
from compilador.exceptions import InvalidPath

def get_path(input_path: str) -> str:
    """Pegar o path correto do usuário"""
    dir_path = f'{PATH}{input_path}'
    if not path.exists(dir_path):
        raise InvalidPath(f'dir path: {dir_path} not exists')
    return dir_path

def get_file(path: str, file_name: str) -> Iterator[str]:
    """Abre um arquivo e retorna seu gerador de caracteres"""
    file_path = f'{path}/{file_name}'
    with open(file_path, 'r') as f:
            yield from f.read()


def main():
    path_dir = '/home/azevedo/Code/compilador/tests/files/input/'
    file_name = 'test1.la'
    file = get_file(path_dir, file_name)
    return file

arquvi = main()
