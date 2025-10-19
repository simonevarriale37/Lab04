class Passeggero:
    def __init__(self, codice, nome, cognome):
    # inizializzo gli attributi della classe Passeggero e li metto privati usando _
        self._codice = codice
        self._nome = nome
        self._cognome = cognome
    # imposto nessuna cabina assegnata inizialmente
        self._cabina = None
    # uso il getter per il codice del passeggero
    @property
    def codice(self):
        return self._codice
    #uso il getter per il nome del passeggero
    @property
    def nome(self):
        return self._nome
    # uso il getter per il cognome del passeggero
    @property
    def cognome(self):
        return self._cognome
    # uso il getter per la cabina assegnata al passeggero
    @property
    def cabina(self):
        return self._cabina
    # uso il setter per la cabina assegnata al passeggero in modo da poter cambiare lo stato della cabina
    @cabina.setter
    def cabina(self, valore):
        self._cabina = valore

    def assegna_cabina(self, cabina):
        self.cabina = cabina

    def __str__(self):
        if self.cabina is not None:
            return f"{self._codice}: {self.nome} {self.cognome} assegnato alla cabina : {self.cabina}"
        else:
            return f"{self._codice} : {self.nome} {self.cognome} non ancora assegnato ad una cabina"