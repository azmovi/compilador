class SymbolEntry:
    def __init__(self, name: str, type: str, kind: str, line: int, fields=None):
        self.name = name
        self.type = type
        self.kind = kind
        self.line = line
        self.fields = fields or []


class SymbolicTable:
    def __init__(self):
        self.symbols: dict[str, SymbolEntry] = {}

    def add(self, name: str, entry: SymbolEntry):
        self.symbols[name] = entry

    def check(self, name: str) -> bool:
        return name in self.symbols

    def get(self, name: str) -> SymbolEntry | None:
        return self.symbols.get(name)
