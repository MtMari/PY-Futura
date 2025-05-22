"""quit    = False
index   = 0

while quit == False:
    index = index + 1               #se scrivi subito print(index + 1) ti printerà for ever SOLO index + 1, cioè 0 + 1, quindi 1!
    
    print(index)

    if index == 10:
        quit = True #oppure scrivi solo break


#name

name    =   input("Enter your name: ")

while name == "":
    print("You did not enter you name.")
    name    =   input("Enter your name: ")

print("Welcome " + name + "!")



#age

age = int(input("Quanti anni hai? "))

while age <= 0:
    print("Inserimento non valido.")
    age = int(input("Per favore, inserisci un numero valido:"))

print("Hai " + str(age) + " anni.")



#cibo: chiedi il cibo preferito e permetti di premere q per terminare

cibo = input("Qual è il tuo cibo preferito? Premere q per uscire. ")

while not cibo == "q":
    print("Il tuo cibo preferito è: " + cibo)
    cibo = input("Quale altro cibo ti piace? Premere q per uscire. ")

print("Arrivederci e grazie.")
"""

#serie di numeri: chiedi d'inserire un numero tra 1 e 10, se diverso, richiedi l'input

num = int(input("Inserisci un numero tra 1 e 10: "))

while num < 1 or num > 10:
    print("Inserimento non valido.")
    num = int(input("Inserisci un numero tra 1 e 10: "))

print("Grazie. Buona giornata!")