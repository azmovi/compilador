from cyclopts import App
from rich.console import Console

from compilador.file_reader import validate_input_file
from compilador.lexical import create_lexical, get_tokens, create_output_file
from compilador.syntactic import run_syntactic_analysis

from .exceptions import InvalidPath

console = Console()
app = App(console=console)


@app.command
def lexical(input_file: str, output_file: str):
    """CLI para o analisador léxico"""
    try:
        input_file_path = validate_input_file(input_file)
            
        # Análise léxica
        token_list = create_lexical(input_file_path)
        create_output_file(output_file, token_list)
        console.print("[green]Análise léxica concluída com sucesso![/green]")
    except InvalidPath:
        console.print_exception()


@app.command
def syntactical(input_file: str, output_file: str):
    try:
        input_file_path = validate_input_file(input_file)
            
        # Análise léxica
        tokens = get_tokens(input_file_path)
        console.print("[green]Análise léxica concluída com sucesso![/green]")
        
        # Análise sintática
        run_syntactic_analysis(tokens, output_file)
        console.print("[green]Análise sintática concluída com sucesso![/green]")   
    except InvalidPath:
        console.print_exception()

