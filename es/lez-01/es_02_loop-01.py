""" 
    chiedi 2 numeri int e che non accetti quantità non numeriche
    01 - riconoscere e stampare a video un messaggio che identifichi il numero più grande e più piccolo ->
    -> chiedi l'inserimento una sola volta. I due decono essere separati da spazi.

    02 - se i due num sono uguali, il programma deve richiedere un numero nuovo div dai due precedenti. Poi ricontrolla il punto 1.

    03 - richiedi inserimento se l'utente inserisce quantità non numeriche
"""

print("Inserisci due numeri interi")

num_01  = int
num_02  = int

if int(input(num_01)) > int(input(num_02)):
    print("Il numero maggiore è ") and print(num_01)
else:
    print("Il numero maggiore è ") and print(num_02)
    
""" if int(input(num_01)) == int(input(num_02)):
    print("Inserimento non valido. Per favore, digita due numeri interi diversi.") """