""" le azioni che compio sullo stato si chiamano METODI
lo stato è chiamato ATTRIBUTI, PROPRIETà o CAMPI. Fisicamente è rappresentato da 1 o più variabili interne alla classe -> SCRIVILI ALL'INTERNO DELLA (funzione della) CLASSE e ricordati che il PRIMO è SELF   """


#self è il riferimento all'oggetto stesso -> serve per far sì che i metodi possano accedere alla memoria dell'oggetto
class Persona_es:

    def chiama(self, ):         #definizione del metodo(, costruttore)
        pass

    """ PERSONA = classe/oggetto
        DEF CHIAMA = metodo, è una funzione speciale perché ha self
        SELF = riferimento all'oggetto stesso
        DOPO SELF = argomenti
    """

    #quando uso questo contratto sto definiendo un'istanza di quella classe -> GLI OGGETTI DI TIPO Persona SONO DETTE ISTANZE DELLA CLASSE -> ne posso creare quante ne voglio

""" 
    alcuni METODI di una classe anno necessariamente definiti, ad       esempio: 
    __init__ -> inizializza (=initialize) i miei attributi/campi/memoria della classe/oggetto -> SEMPRE PRESENTE O LE TUE CLASSI NON HANNO STATO
    __new__  -> alloco in memoria [dimenticalo lmao]
    ... (dunder method = metodi a doppio underscore)
"""

class Persona:

    def __init__(self, nome, eta, altezza, cf): #, nome etc=etichette
        self.nome        = nome
        self.eta         = eta          #contenuto inizializzato alle rispettive etichette
        self.altezza     = altezza
        self.cf          = cf

    def chiama(self, ):
        print("Ciao " + self.nome)

#creiamo un'istanza di una persona -> dare TUTTI i parametri

andrea = Persona('andrea', 27, 1.75, 'CF123456')  #nuovo tipo di dato definito chiamato Persona, lo puoi usare manipolando la memoria data in precedenza

#su andrea possiamo chiamare la funzione/metodo chiama

andrea.chiama()
#come richiamo l'interno, gli ARGOMENTI
andrea.eta
andrea.altezza
andrea.cf

#cosa succede se l'oggetto ha dati sensibili? -> qui NON c'è la differenza tra memoria nascosta e non -> PYTHON è PUBBLICO DI DEFAULT!

#'self._altezza' -> con l'UNDERSCORE significa che è privato, ma è SOLO NOMENCLATURA --> quando li trovi, significa che vanno usati ad uso esclusivo interno alla classe --> non hanno effetto
#||=> VALE ANCHE PER I METODI


giulia = Persona('giulia', 33, 1.67, 'CF789012')

giulia.chiama()

