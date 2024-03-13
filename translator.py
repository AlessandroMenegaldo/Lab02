import dictionary


class Translator:

    def __init__(self):
        self.dizionario=dictionary.Dictionary()
        pass

    def printMenu(self):
        print("-----------------------------")
        print("   Traslator Alien-Italian  ")
        print("-----------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Exit")
        print("-----------------------------")
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        pass



    def loadDictionary(self, dict):
        """
        Legge il file dato come imput creando dizionario
        :param dict: file testo contentente dizionario
        :return: null
        """

        infile = open(dict, "r")
        contenuto_file = infile.read()
        infile.close()

        parole = contenuto_file.strip().split('\n')


        for p in parole:
            lista_significati=[]
            campi=p.strip().split(" ")
            lista_significati.append(campi[1])
            self.dizionario.addWord(campi[0], lista_significati)
        pass

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        campi= entry.strip().lower().split(" ")
        meanings=[]
        for c in campi:
            if c==campi[0]:
                pass
            meanings.append(c)
        self.dizionario.addWord(campi[0],meanings)
        pass

    def handleTranslate(self, query):
        """
        cerca traduzione: fa affidamento a translate di dictionary che dato in ingresso una parola aliena
        restituisce il significato italiano
        :param query: query in ingresso terminale
        :return: traduzione
        """
        return self.dizionario.translate(query.lower())


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self.dizionario.translateWordWildCard(query.lower())

        pass
