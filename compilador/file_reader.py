from os import path
from typing import Iterator
from compilador.constants import PATH
from compilador.exceptions import InvalidPath

from antlr4 import InputStream, CommonTokenStream
from compilador.parser.LangAlg import LangAlg

def get_path(input_path: str) -> str:
    """Pegar o path correto do usuário"""
    dir_path = f'{PATH}{input_path}'
    if not path.exists(dir_path):
        raise InvalidPath(f'dir path: {dir_path} not exists')
    return dir_path

def get_file_content(path: str, file_name: str) -> str:
    """Abre um arquivo e retorna seu gerador de caracteres"""
    file_path = f'{path}/{file_name}'
    with open(file_path, 'r') as f:
        return f.read()

def get_token_stream(file_content: str):
    input_stream = InputStream(file_content)
    print(input_stream)
    tokens =  CommonTokenStream(LangAlg(InputStream(file_content)))
    print(tokens)

def main():
    path_dir = '/home/azevedo/Code/compilador/tests/files/input/'
    file_name = 'test1.la'
    file = get_file_content(path_dir, file_name)
    tokens = get_token_stream(file)
    print(tokens)
    return tokens

main()
