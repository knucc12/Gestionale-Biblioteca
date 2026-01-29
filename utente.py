import random

class Utente:
    def __init__(self, nome):
        self.nome = nome
        self.numero_tessera = random.randint(100000, 999999)

    def __eq__(self, other):
        if not isinstance(self, other):
            return False
        
        return self.nome == other.nome and self.numero_tessera == other.numero_tessera
    
    def __repr__(self):
        return f"Utente(nome = {self.nome}; numero tessera = {self.numero_tessera})"
    