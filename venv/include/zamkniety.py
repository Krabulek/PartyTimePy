class Otwarty(Obiekt):
    def __init__(self, n, a, p, t):
        super().__init__(n, a)
        self.__pojemnosc = p
        self.__typ = t

    @property
    def nazwa(self):
        super().nazwa()

    @property
    def adres(self):
        super().adres()

    @property
    def pojemnosc(self):
        return self.__pojemnosc

    @property
    def typ(self):
        return self.__typ

    def __str__(self):
        return f"{self.nazwa}, adres: {self.adres}, powierzchnia {self.pojemnosc} - typ {self.typ}"