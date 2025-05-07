class SymbolicTable:
    def __init__(self):
        self.symbols: dict[str, str] = {}

    def add(self, name: str, tipe: str):
        self.symbols[name] = tipe

    def check(self, name: str):
        return name in self.symbols.keys()
    
    def get(self, name: str):
        return self.symbols[name]

        