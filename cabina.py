class Cabina:
    def __init__(self, codice, num_letti, num_ponte, prezzo_base):
        # inizializzo gli attributi della classe Cabina e li metto privati usando _
        self._codice = codice
        self._num_letti = int(num_letti)
        self._num_ponte = int(num_ponte)
        self._prezzo_base = float(prezzo_base)
        # imposto la cabina inizialmente libera
        self._disponibile = True
        # imposto nessun passeggero ancora assegnato
        self._passeggero = None
    # uso il getter per il codice della cabina
    @property
    def codice(self):
        return self._codice
    # uso il getter per la disponibilità della cabina
    @property
    def disponibile(self):
        return self._disponibile
    # uso il setter per la disponibilità perchè così permette di cambiare da Disponibile a Occupata
    @disponibile.setter
    def disponibile(self, valore):
        self._disponibile = valore
    # uso il getter per il prezzo finale della cabina
    @property
    def prezzo(self):
        return self._prezzo_base
    # faccio la funzione assegna_passeggero per assegnare un passeggero ad una cabina e renderla occupata
    def assegna_passeggero(self, passeggero):
        self._passeggero = passeggero
        self._disponibile = False

    def __str__(self):
        if self._disponibile:
            stato = "Disponibile"
        else:
            stato = "Occupato"
        return f"{self._codice} : Standard | {self._num_letti} letti - Ponte {self._num_ponte} - Prezzo {self.prezzo} euro - {stato}"
    # uso il metodo __lt__ per fare il confronto tra i prezzi
    def __lt__(self, other):
        return self.prezzo < other.prezzo

# definisco la classe Cabina_con_animali che sarebbe la classe figlia di Cabina a cui viene aggiunto
# l'attributo max_animali per il numero di animali
class Cabina_con_animali(Cabina):
    def __init__(self, codice, num_letti, num_ponte, prezzo_base, max_animali):
        super().__init__(codice, num_letti, num_ponte, prezzo_base)
        self._max_animali = int(max_animali)
    # uso il getter per il prezzo con l'aggiunta della percentuale per ogni animale
    @property
    def prezzo(self):
        return self._prezzo_base * (1 + 0.10 * self._max_animali)

    def __str__(self):
        if self._disponibile:
            stato = "Disponibile"
        else:
            stato = "Occupato"
        return f"{self._codice} : Animali | {self._num_letti} letti - Ponte {self._num_ponte} - Prezzo {self.prezzo} euro - Max animali {self._max_animali} - {stato}"

# definisco la classe CabinaDeluxe che sarebbe la classe figlia di Cabina a cui viene aggiunto
# l'attributo stile per indicare lo stile della cabina
class CabinaDeluxe(Cabina):
    def __init__(self, codice, num_letti, num_ponte, prezzo_base, stile):
        super().__init__(codice, num_letti, num_ponte, prezzo_base)
        self._stile = stile
    # uso il getter per il prezzo con l'aggiunta della percentuale per la cabina deluxe
    @property
    def prezzo(self):
        return self._prezzo_base * 1.20

    def __str__(self):
        if self._disponibile:
            stato = "Disponibile"
        else:
            stato = "Occupato"
        return f"{self._codice} : Deluxe {self._stile} | {self._num_letti} letti - Ponte {self._num_ponte} - Prezzo {self.prezzo} euro - {stato}"


