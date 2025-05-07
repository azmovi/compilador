from cyclopts import App
from rich.console import Console

from compilador.lexical import run_lexical_analysis
from compilador.syntactic import run_syntactic_analysis
from compilador.semantic import run_semantic_analysis

console = Console()
app = App(console=console)


@app.command
def lexical(input_file: str, output_file: str):
    """Analisador léxico"""
    try:
        run_lexical_analysis(input_file, output_file)
        console.print('[green]Análise léxica concluída com sucesso![/green]')
    except ValueError:
        console.print_exception()


@app.command
def syntactical(input_file: str, output_file: str):
    """Analisador sintático"""
    try:
        run_syntactic_analysis(input_file, output_file)
        console.print('[green]Análise sintática concluída com sucesso![/green]')
    except ValueError:
        console.print_exception()


@app.command
def semantical(input_file: str, output_file: str):
    """Analisador semântico"""
    try:
        run_semantic_analysis(input_file, output_file)
        console.print('[green]Análise semântica concluída com sucesso![/green]')
    except ValueError:
        console.print_exception()