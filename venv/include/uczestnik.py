class Uczestnik:

    ile = 0

    def __init__(self, l, i, n):
        self.__login = l
        self.__imie = i
        self.__nazwisko = n

        Uczestnik.ile += 1
        self.ktory = Uczestnik.ile

    @property
    def login(self):
        return self.__login

    @property
    def imie(self):
        return self.__imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @staticmethod
    def policz():
        return Uczestnik.ile

    def __str__(self):
        return f"{self.ktory}. {self.login} {self.imie} {self.nazwisko}"