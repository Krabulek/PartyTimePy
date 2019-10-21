from zespol import Zespol

class Impreza:

    ile = 0

    def __init__(self, n, r, o, d, m, y):
        self.__nazwa = n
        self.__rodzaj = r
        self.__organizator = o
        self.__dzien = d
        self.__miesiac = m
        self.__rok = y
        self.harmonogram = []
        self.klienci = []
        self.obiekt = "brak"

        Impreza.ile += 1
        self.ktory = Impreza.ile

    @property
    def nazwa(self):
        return self.__nazwa

    @property
    def rodzaj(self):
        return self.__rodzaj

    @property
    def organizator(self):
        return self.__organizator

    @property
    def dzien(self):
        return self.__dzien

    @property
    def miesiac(self):
        return self.__miesiac

    @property
    def rok(self):
        return self.__rok

    @staticmethod
    def policz():
        return Impreza.ile

    def __str__(self):
        return f"{self.ktory}. {self.nazwa} ({self.rodzaj}), organizowana przez {self.organizator}, data: {self.dzien}.{self.miesiac}.{self.rok}"

    def dodajZespol(self, z):
        self.harmonogram.append(z)

    def usunZespol(self, z):
        if z in self.harmonogram:
            self.harmonogram.remove(z)

    def dodajUczestnika(self, u):
        self.klienci.append(u)
        
    def usunUczestnika(self, u):
        if u in self.klienci:
            self.klienci.remove(u)

    def dodajObiekt(self, o):
        if self.obiekt == "brak":
            self.obiekt = o

    def usunObiekt(self):
        if self.obiekt != "brak":
            self.obiekt = "brak"

    def usunWszystko(self):
        self.harmonogram.clear()
        self.klienci.clear()

    def wyswietlZespoly(self):
        for z in self.harmonogram:
            print(z)

    def wyswietlUczestnikow(self):
        for u in self.klienci:
            print(u)