from compilador.parser.LangAlgVisitor import LangAlgVisitor
from compilador.scope import Scope
from compilador.symbolsTable import SymbolEntry, SymbolicTable
from compilador.syntactic import get_parser

class LangAlgSemantic(LangAlgVisitor):
    def __init__(self):
        self.scopes = Scope()
        self.errors: list[str] = []

    def visitPrograma(self, ctx):
        super().visitPrograma(ctx)
        for e in self.errors:
            print(e)
        print("Fim da compilação")
        return None
    
    def addEntry(self, name, type_, kind, line, fields=None):
        entry = SymbolEntry(name=name, type_=type_, kind=kind, line=line, fields=fields)
        try:
            self.scopes.currentScope().add(entry)
        except ValueError as ve:
            self.errors.append(str(ve))

    def visitDecl_const(self, ctx):
        # CONSTANTE IDENT DOIS_PONTOS tipo_basico ATRIB expressao
        name = ctx.IDENT().getText()
        line = ctx.IDENT().symbol.line
        type_ = ctx.tipo_basico().getText()
        
        self.addEntry(name, type_, 'const', line)

        return super().visitDecl_const(ctx)

    def visitDecl_var(self, ctx):
        # DECLARE IDENT (VIRGULA IDENT)* DOIS_PONTOS tipo
        if ctx.tipo().tipo_basico():
            type_ = ctx.tipo().tipo_basico().getText()
        elif ctx.tipo.IDENT():
            type_ = ctx.tipo.IDENT().getText()
        else: 
            type_ = 'ponteiro'
        for ident in ctx.IDENT():
            name = ident.getText()
            line = ident.symbol.line
            self.addEntry(name, type_, 'var', line)
        return super().visitDecl_var(ctx)
    
    def visitDecl_tipo(self, ctx):
        # TIPO IDENT DOIS_PONTOS REGISTRO decl_var* FIM_REGISTRO
        name = ctx.IDENT().getText()
        line = ctx.IDENT().symbol.line

        fields = set()
        for decl_var in ctx.decl_var():
            var_type = decl_var.tipo().getText()
            for ident in decl_var.IDENT():
                field_name = ident.getText()
                fields.add((field_name, var_type))

        self.addEntry(name, 'registro', 'tipo', line, fields)
        
        return super().visitDecl_tipo(ctx)
    
    def visitDecl_proc(self, ctx):
        # PROCEDIMENTO IDENT params? bloco FIM_PROCEDIMENTO

        return super().visitDecl_proc(ctx)
    
    def visitDecl_func(self, ctx):
        # FUNCAO IDENT params? DOIS_PONTOS tipo bloco FIM_FUNCAO
        return super().visitDecl_func(ctx)

def run_semantic_analysis():
    tree =  get_parser().programa()
    semantic = LangAlgSemantic()
    semantic.visitPrograma(tree)

