valid_types = 'inteiro', 'real', 'literal', 'logico', 'registro'
invalid = 'invalid'

class SymbolEntry:
    def __init__(self, name: str, type_: str, kind: str, line: int, fields=None):
        self.name = name   
        self.type = type_  
        self.kind = kind  
        self.line = line   
        self.fields = fields or []

class SymbolicTable:
    def __init__(self):
        self.symbols: dict[str, SymbolEntry] = {}

    def add(self, name: str, entry: SymbolEntry):
        if entry.type not in valid_types:
            raise ValueError(f"Linha {entry.line}: tipo {entry.type} nao declarado")
        if self.check(name):
            raise ValueError(f"Linha {entry.line}: identificador {entry.name} ja declarado anteriormente")
        self.symbols[name] = entry

    def check(self, name: str) -> bool:
        return name in self.symbols
    
    def get(self, name: str) -> SymbolEntry | None:
        return self.symbols.get(name)