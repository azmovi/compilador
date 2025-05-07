from compilador.symbolsTable import SymbolicTable

class Scope:
    
    def __init__(self):
        self.tablesList: list[SymbolicTable] = []
        self.createScope()

    def createScope(self):
        self.tablesList.append(SymbolicTable()) 

    def currentScope(self) -> SymbolicTable:
        return self.tablesList[-1]
    
    def searchNestedScope(self, name: str) -> SymbolicTable | None:
        """
        Procura de dentro para fora: retorna a tabela onde name foi
        encontrado, ou None se não achar em nenhum escopo.
        """
        for table in reversed(self.tablesList):
            if table.check(name):
                return table
        return None
    
    def leaveScope(self):
        self.tablesList.pop()
