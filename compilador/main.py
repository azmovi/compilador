from cyclopts import App
from rich.console import Console

from compilador.file_reader import get_file_path
from compilador.lexical import create_lexical

from .exceptions import InvalidPath

console = Console()
app = App(console=console)


@app.default
def main(input_file: str, output_file: str):
    """Cli para o analisador léxico"""
    try:
        input_file_path, output_file_path = get_file_path(input_file, output_file)
        return create_lexical(input_file_path, output_file_path)
    except InvalidPath:
        console.print_exception()
