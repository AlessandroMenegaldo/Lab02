import re
class Dictionary:
    def __init__(self):
        self._significati={}
        pass


    def addWord(self, word, meanings):
        # controllo se  esiste parola esiste gia nel dizionario
        if self.esisteWord(word):
            for m in meanings:
                if not self.esisteSignificato(word,m):
                    self.significati[word].append(meanings)
        else:
            self._significati[word] = meanings
        pass

    def translate(self, word):
        return self._significati[word]

    def translateWordWildCard(self, query):
        lista=[]
        reg = re.compile(query.replace("?", "."))
        for alien_Word in self._significati:
            match = bool(re.match(reg, alien_Word))
            if match:
                lista.append(alien_Word)

        tradotti=[]
        for word in lista:
            tradotti.append(self.translate(word))
        return tradotti
        pass

    def esisteWord(self, word):
        """
        Verifica se parola già presente nel dizionario
        :param word: parola da cercare
        :return: True se già presente
        """
        for parola in self._significati:
            if parola==word:
                return True
        return False

    def esisteSignificato(self, word,meaning):
        """
        Verifica se significato già presente per quella parola
        :param word: significato da cercare e parola tradotta
        :return: True se già presente
        """
        for m in self.significati[word]:
            if m == meaning:
                return True
        return False


    @property
    def significati(self):
        return self._significati

