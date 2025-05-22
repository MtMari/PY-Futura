#soluzione esercizio slide 78
#CONSEGNA: Scrivere un programma che chieda in input due numeri interi separati da spazio e che controlli l'eventuale inserimento di quantità non numeriche
while True:
    stringa_fornita = input("Inserisci due numeri interi separati da spazio: ")

    # gestiamo il caso in cui la stringa cominci con lo spazio
    nuova_stringa = stringa_fornita.lstrip(' ').rstrip(' ')
    if stringa_fornita.find(' ') == -1:
        #spazio non trovato
        print("Non hai inserito due quantità numeriche separate da spazio.")
    else:
        #sicuro che ci sia uno spazio.
        stringhe_separate = nuova_stringa.split(' ')

        print(stringhe_separate[0])             #se 'print(stringhe_separate? OUTPUT: ['3', '4'] -> [0] E [1] è PERCHé è UN ARRAY)
        print(stringhe_separate[1])

        #controlla che l'input inserito non sia troppo lungo -> SOLO 2 QUANTITà
        if len(stringhe_separate) == 2:

            if stringhe_separate[0].isdigit() and stringhe_separate[1].isdigit():
                #ho due stringhe che contengono quantità numeriche
                num1 = int(stringhe_separate[0])
                num2 = int(stringhe_separate[1])

                if num1 >= num2:
                    print("Il numero 1 è più grande del numero 2")
                else:
                    print("Il numero 2 è più grande del numero 1")
                break
            else:
                print("Mi hai inserito due quantità errate"
                )
        else:
            print("Non hai inserito le quantità richieste.")
    print("Ciao")

#ROBE DA SISTEMARE:
#           1)          Se ci sono più numeri -> inserirne 2 => OK
#           2)          Utilizzare un loop x controllare corretteza quantità e richiedere eventuale input => OK
#           3)          Cosa succede se metto una , come separatore => OK

