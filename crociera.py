import csv
from cabina import Cabina, CabinaDeluxe, Cabina_con_animali
from passeggeri import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self._cabine_disponibili = []
        self._passeggeri_disponibili = []
    # uso il getter per il nome della crociera
    @property
    def nome(self):
        return self._nome
    # uso il setter per il nome della crociera perchè così posso modificarlo
    @nome.setter
    def nome(self, nuovo_nome):
        self._nome = nuovo_nome
    # uso il getter per le cabine disponibili
    @property
    def cabine_disponibili(self):
        return self._cabine_disponibili
    # uso il getter per i passeggeri disponibili
    @property
    def passeggeri_disponibili(self):
        return self._passeggeri_disponibili


    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        try:
            with open(file_path, "r", encoding = 'utf-8') as file:
                for riga in file:
                    campi = riga.strip().split(',')
                    # controllo il codice se inizia per CAB o per P per capire se è il codice di una
                    # cabina o di un passeggero
                    codice = campi[0]
                    if codice[:3] == 'CAB':
                        num_letti, num_ponte, prezzo_base = campi[1], campi[2], campi[3]
                        # controllo se ha un campo aggiuntivo
                        if len(campi) == 4:
                            cabina = Cabina(codice, num_letti, num_ponte, prezzo_base)
                        # se il campo è un numero allora il campo aggiuntivo è il numero degli animali
                        # e la cabina è di tipologia Cabina_con_animali
                        elif campi[4].isdigit():
                            max_animali = int(campi[4])
                            cabina = Cabina_con_animali(codice, num_letti, num_ponte, prezzo_base, max_animali)
                        else:
                        # se il campo è una stringa allora il campo aggiuntivo è lo stile e la cabina
                        # è di tipologia CabinaDeluxe
                            stile = campi[4]
                            cabina = CabinaDeluxe(codice, num_letti, num_ponte, prezzo_base, stile)
                        self._cabine_disponibili.append(cabina)
                    elif codice[:1] == 'P':
                        nome, cognome = campi[1], campi[2]
                        passeggero = Passeggero(codice, nome, cognome)
                        self._passeggeri_disponibili.append(passeggero)
                # quando carico il file faccio la stampa dividendo le cabine e i passeggeri
                print("CABINE:\n")
                for cabina in self._cabine_disponibili:
                    print(cabina)
                print("")
                print("PASSEGGERI:\n")
                for passeggero in self._passeggeri_disponibili:
                    print(passeggero)
        except FileNotFoundError:
            exit("File non trovato")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # Cerco la cabina
        cabina = None
        for c in self._cabine_disponibili:
            if c.codice == codice_cabina:
                cabina = c
                break
        # Cerco il passeggero
        passeggero = None
        for p in self._passeggeri_disponibili:
            if p.codice == codice_passeggero:
                passeggero = p
                break
        # controllo se esiste la cabina o il passeggero
        if cabina is None or passeggero is None:
            raise ValueError("cabina o passeggero non trovato")
        # controllo se la cabina è già occupata
        if not cabina.disponibile :
            raise ValueError("cabina già occupata")
        # controllo se il passeggero è già stato assegnato
        if passeggero.cabina is not None:
            raise ValueError("passeggero già assegnato ad un'altra cabina")
        cabina.disponibile = False
        passeggero.cabina = cabina

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        return sorted(self._cabine_disponibili)
    # Non metto key... lambda... perchè nella classe cabina ho usato il metodo __lt__
    # che fa già il confronto sul prezzo


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        for passeggero in self._passeggeri_disponibili:
            print(passeggero)



