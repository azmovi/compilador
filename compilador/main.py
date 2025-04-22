from os import listdir
from cyclopts import App
from rich.console import Console

from .exceptions import InvalidPath, InvalidFile
from .utils import get_file, get_path


console = Console()
app = App(console=console)

@app.default
def main(input_path: str):
    try:
        path = get_path(input_path)
        for file_name in listdir(path):
            file = get_file(path, file_name)
            token_list = get_tokens(file)

    except (InvalidPath, InvalidFile):
        console.print_exception()

