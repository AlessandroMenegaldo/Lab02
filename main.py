import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIniziale = input()


    # Add input control here!



    if int(txtIniziale) == 1:

        print("Ok, quale parola devo aggiungere?")
        txtIn = input()
        if not txtIn.isalpha():
            print("errore  di inserimento")
            pass

        t.handleAdd(txtIn)
        print("Aggiunta!")
        pass

    if int(txtIniziale) == 2:
        print("Ok, quale parola devo cercare?")
        txtIn = input()
        if not txtIn.isalpha():
            print("errore  di inserimento")
            pass
        print(t.handleTranslate(txtIn))
        pass

    if int(txtIniziale) == 3:
        print("Modalità WildCard: \n -quando nella "
              "parola aliena compare il simbolo “?”, il carattere "
              "corrispondente può essere qualsiasi-")
        print("Ok, quale parola devo cercare?")
        txtIn = input()
        if not txtIn.isalpha():
            print("errore  di inserimento")
            pass
        print(t.handleWildCard(txtIn))
        pass
    if int(txtIniziale) == 4:
        break
