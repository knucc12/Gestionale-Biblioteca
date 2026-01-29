class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo = []
        # self.libri_in_prestito = []
        self.utenti = []

    def __eq__(self, other):
        if not isinstance(self, other):
            return False
        
        return self.nome == other.nome
    
    def __repr__(self):
        return f"Biblioteca(nome = {self.nome}; libri = {self.catalogo})"
    
    def aggiungi_libro(self, libro):
        if libro in self.catalogo:
            print("Libro già presente nel catalogo")
        else:
            self.catalogo.append(libro)
            print("Il libro è stato aggiunto al catalogo") 
    
    def libreria_utente(self, utente):
        self.utenti.append(utente)
        for utente in self.utenti:
            self.libri_in_prestito = []

    # risolvere bug prestito
    def prestito(self, libreria, libro):
        if libro in self.catalogo and len(self.libri_in_prestito) <= 3:
            self.libri_in_prestito.append(libro)
            self.catalogo.remove(libro)
            print("Il libro è stato preso in prestito")
        else:
            print("Impossibile prendere in prestito il libro")


    def restituisci(self, utente, libro):
        if libro in self.libri_in_prestito:
            self.catalogo.append(libro)
            self.libri_in_prestito.remove(libro)