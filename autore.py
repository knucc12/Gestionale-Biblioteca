class Autore:
    def __init__(self, nome, nazionalita):
        self.nome = nome
        self.nazionalita = nazionalita

    def __eq__(self, other):
        if not isinstance(self, other):
            return False
        
        return self.nome == other.nome and self.nazionalita == other.nazionalita
    
    def __repr__(self):
        return f"Autore(nome = {self.nome}; nazionalità = {self.nazionalita})"