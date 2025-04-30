from cyclopts import App
from rich.console import Console

from compilador.file_reader import validate_input_file
from compilador.lexical import run_lexical_analysis
from compilador.syntactic import run_syntactic_analysis

from .exceptions import InvalidPath

console = Console()
app = App(console=console)


@app.command
def lexical(input_file: str, output_file: str):
    """CLI para o analisador léxico"""
    try:
        input_file_path = validate_input_file(input_file)
        run_lexical_analysis(input_file_path, output_file)
        console.print('[green]Análise léxica concluída com sucesso![/green]')
    except InvalidPath:
        console.print_exception()


@app.command
def syntactical(input_file: str, output_file: str):
    try:
        input_file_path = validate_input_file(input_file)
        run_syntactic_analysis(input_file_path, output_file)
        console.print('[green]Análise sintática concluída com sucesso![/green]')
    except InvalidPath:
        console.print_exception()
