class Obiekt:

    ile = 0

    def __init__(self, n, a):
        self.__nazwa = n
        self.__adres = a
        self.imprezki = []

        Obiekt.ile += 1
        self.ktory = Obiekt.ile

    @property
    def nazwa(self):
        return self.__nazwa

    @property
    def adres(self):
        return self.__adres

    @staticmethod
    def policz():
        return Obiekt.ile

    def __str__(self):
        return f"{self.ktory}. {self.nazwa}, adres: {self.adres}"

    def dodajImpreze(self, i):
        self.imprezki.append(i)

    def usunImpreze(self, i):
        if i in self.imprezki:
            self.imprezki.remove(i)

    def wyswietlImprezy(self):
        for i in self.imprezki:
            print(i)