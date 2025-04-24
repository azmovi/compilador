from cyclopts import App
from rich.console import Console

from compilador.file_reader import validate_input_file
from compilador.lexical import create_lexical

from .exceptions import InvalidPath

console = Console()
app = App(console=console)


@app.default
def main(input_file: str, output_file: str):
    """CLI para o analisador léxico"""
    try:
        input_file_path = validate_input_file(input_file)
        return create_lexical(input_file_path, output_file)
    except InvalidPath:
        console.print_exception()
