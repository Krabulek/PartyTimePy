class Zespol:

    ile = 0

    def __init__(self, n, g, p):
        self.__nazwa = n
        self.__gatunek = g
        self.__kraj = p

        Zespol.ile += 1
        self.ktory = Zespol.ile

    @property
    def nazwa(self):
        return self.__nazwa

    @property
    def gatunek(self):
        return self.__gatunek


    @property
    def kraj(self):
        return self.__kraj

    def __str__(self):
        return f"{self.ktory}. {self.nazwa} ({self.gatunek}) - {self.kraj}"