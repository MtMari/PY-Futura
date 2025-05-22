"""quit = False

if quit == False:
    print("quit è settato su false")
else:
    print("quit è settato su true")


#numero
numero = int(input("Digita un numero:"))

if numero > 0:
    print("Il numero è maggiore di 0")
elif numero < 0:
    print("Il numero è minore di 0")
else:
    print("Il numero è uguale a 0")

#età
età = int(input("Per accedere al servizio inserisci la tua età: "))

if età >= 18:
    print("Accesso consentito")
else:
    print("Accesso negato") 

#età_sign_up
età_sign_up = int(input("Per registrarti inserisci la tua età: "))

if 18 <= età_sign_up < 100:  #età_sign_up >= 18
    print("Registrazione avvenuta con successo. Benvenuto!")
elif età_sign_up >= 100:
    print("Sei troppo vecchio per registrarti a questo servizio.")
elif 0 < età_sign_up < 18:
    print("Registrazione fallita. Devi avere almeno 18 anni per registrarti.")
else:
    print("Inserimento non valido.") """

#es_01: chiedi se vuole del cibo, poi printa un frase idonea per ogni situazione

response = input("Would you like some food? (Y/N)")

if response == "Y" or "y":
    print("You can find the food isle at 3rd floor.")
elif response == "N" or "n":
    print("Then there is nothing I can do to help you.")
