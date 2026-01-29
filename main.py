from utente import Utente
from biblioteca import Biblioteca
from autore import Autore
from libro import Libro
from operazioni import Operazione

if __name__ == "__main__":

    u1 = Utente("Kasy")
    print(u1)

    

    a1 = Autore("Dan Brown", "Americano")

    b1 = Biblioteca("Biblioteca1")
    l1 = Libro("Angeli e Demoni", "3849716352384", a1)
    l2 = Libro("Il Codice Da Vinci", "38594081748954", a1)

    b1.aggiungi_libro(l1)
    libreria1 = b1.libreria_utente(u1)
    b1.prestito(libreria1, l1)
    b1.prestito(libreria1, l1)
    b1.prestito(libreria1, l2)