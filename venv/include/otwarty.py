class Otwarty(Obiekt):
    def __init__(self, n, a, p):
        super().__init__(n, a)
        self.powierzchnia = p

    @property
    def nazwa(self):
        super().nazwa()

    @property
    def adres(self):
        super().adres()

    @property
    def powierzchnia(self):
        return self.__powierzchnia

    def __str__(self):
        return f"{self.nazwa}, adres: {self.adres}, powierzchnia {self.powierzchnia}"