
#CONTRATTO FUNZIONE: 
"""va rigorosamente rispettato -> se la quantità di argomenti non torna, py non funziona --> IL CONTRATTO E' VINCOLANTE """


"""puoi usare le annotations per indicare a chi arriva dopo il tipo di variabile"""
def nome_funzione(argomento1, argomento2 : int, argomento3):
    ...#codice eseguito ogni volta che richiami la funzione

""" puoi usare le annotations anche al risultato della funzione, che sarà utile per il resto dei programmatori del team """
def nome_funzione(argomento1, argomento2 : int, argomento3) -> float:
    ...


def somma (num1 :float, num2 :float) -> float:
    somma = num1 + num2  
    #"return" equivale al risultato della funzione
    return somma    
    """#si può scrivere anche direttamente 'return num1 + num2', ma così facendo non allochi il risultato ad una nuova variabile-> entrambi i metodi vanno bene"""

risultato = 0
#CHIAMATA FUNZIONE: 
"""se non usi 'return' il contenuto sarà 'None' perché non hai salvato il risultato della funzione con return! RICORDA: le funzioni restituiscono un valore e puoi muoiono, se non salvi il risultato, lo perdi"""
risultato = somma(3, 2)                 #CHIAMATA 1

print(risultato)

risultato = somma(risultato + 4)        #CHIAMATA 2

""" --------------------------------------------------------------"""

##ARGOMENTI DEFAULT FUNZIONE -> 
"""per evitare di richiamare tutti gli argomenti di una funzione pur rispettandone il contratto --> se definisco un argomenti di default con il rispettivo valore, anche se non lo richiamo specificatamente py funzionerà lo stesso perché ne conosce il valore
ATTENZIONE: gli argomenti di default vanno elencati SEMPRE DOPO nella definizione E nella chiamata della funzione"""

def decremento(sottraendo, sottratto=1):
    return sottraendo - sottratto

risultato_sottrazione = decremento(5)   
print(risultato_sottrazione)

#Se il programmatore definisce l'argomento di default, ciò che definisce sovracsriverà il valore di deffault """

risultato_sottrazione = decremento(risultato_sottrazione, 2)
print(risultato_sottrazione)

#qui, oltre a definire il valore dell'argomento di default, aggiungo la SPECIFICA DEL NOME dell'argomento di defualt
risultato_sottrazione = decremento(risultato_sottrazione, sottratto=2)
print(risultato_sottrazione)


#FUNZIONI CON ARGOMENTI CON QUANTITà ARGOMENTI VARIABILI A RUNTIME/MUTEVOLI
""" * (=annotazione ad asterisco) significa che prende in ingresso un numero variabile di argomenti -> 'args' è un nome creato da noi"""

#usato per somme, funzioni di cui non si sa l'input o per implementazioni/estensioni future alla loro logica
def funzione_1(*args):          
    pass

risultato_funzione_1 = funzione_1(1, 2, 3, 4, 5)
risultato_funzione_2 = funzione_1(1, 2, 3, 4, 5, 10, 11)