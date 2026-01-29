import datetime

class Operazione:
    def __init__(self, tipo):
        self.tipo = tipo
        self.data = datetime.now()

    def __eq__(self, other):
        if not isinstance(self, other):
            return False
        
        return self.tipo == other.tipo and self.data == other.data
    
    def __repr__(self):
        return f"Operazione(tipo = {self.tipo}; data = {self.data})"