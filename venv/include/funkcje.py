import sys
from impreza import Impreza
from obiekt import Obiekt
from uczestnik import Uczestnik
from zespol import Zespol

imprezy = {}
obiekty = {}
uczestnicy = {}
zespoly = {}

def aFunkcja():
    i1 = Impreza("Openair", "festwial", "PP", "1", "1", "1")
    i2 = Impreza("Grillowanie", "festiwal", "UAM", "1", "1", "1")

    imprezy[i1.nazwa] = i1
    imprezy[i2.nazwa] = i2

    z1 = Zespol("Kult", "rock", "Polska")
    z2 = Zespol("Rammstein", "rock", "Niemcy")

    zespoly[z1.nazwa] = z1
    zespoly[z2.nazwa] = z2

    u1 = Uczestnik("ola", "Ola", "Cielas")
    u2 = Uczestnik("katarzyna", "Katarzyna", "Cielas")

    uczestnicy[u1.login] = u1
    uczestnicy[u2.login] = u2

    o1 = Obiekt("Hala", "Poznan")
    o2 = Obiekt("Atlas Arena", "Lodz")

    obiekty[o1.nazwa] = o1
    obiekty[o2.nazwa] = o2
    print("Dodajesz obiekt\n")
    nazwa = input("Nazwa obiektu: ")
    adres = input('Adres obiektu: ')
    wybor = input('Typ obiektu (1-otwarty, 2-zamkniety): ')
    if wybor == '1':
        powierzchnia = input('Podaj powierzchnie')
        ot = Otwarty(nazwa, adres, powierzchnia)
        print(ot)
    if wybor == '2':
        pojemnosc = input('Podaj pojemnosc: ')
        typ = input('Podaj typ: ')
        zam = Zamkniety(nazwa, adres, pojemnosc, typ)
        print(zam)

    if nazwa in obiekty:
        print('Obiekt o takiej nazwie juz istnieje!')
    else:
        o = Obiekt(nazwa, adres)
        obiekty[o.nazwa] = o
        print('Dodano obiekt: ')
        print(o)


def bFunkcja():
    print("Dodajesz impreze\n")
    nazwa = input('Nazwa wydarzenia: ')
    rodzaj = input('Rodzaj wydarzenia: ')
    organizator = input('Organizator wydarzenia: ')
    dzien = input('Dzien: ')
    miesiac = input('Miesiac: ')
    rok = input('Rok: ')

    if nazwa in imprezy:
        print('Impreza o takiej nazwie juz istnieje!')
    else:
        i = Impreza(nazwa, rodzaj, organizator, dzien, miesiac, rok)
        imprezy[i.nazwa] = i
        print("Dodano impreze: ")
        print(i)


def cFunkcja():
    print("Dodajesz uczestnika\n")
    login = input('Login uczestnika: ')
    imie = input('Imie uczestnika: ')
    nazwisko = input('Nazwisko uczestnika: ')

    if login in uczestnicy:
        print('Login juz zajety!')
    else:
        u = Uczestnik(login, imie, nazwisko)
        uczestnicy[u.login] = u
        print("Dodano uczestnika: ")
        print(u)


def dFunkcja():
    print("Dodajesz zespol\n")
    nazwa = input('Nazwa zespolu: ')
    gatunek = input('Gatunek: ')
    kraj = input('Kraj pochodzenia: ')

    if nazwa in zespoly:
        print('Zespol o podanej nazwie juz istnieje!')
    else:
        z = Zespol(nazwa, gatunek, kraj)
        zespoly[z.nazwa] = z
        print("Dodano zespol: ")
        print(z)


def eFunkcja():
    print("Dodajesz obiekt do imprezy\n")
    nazwaI = input('Nazwa imprezy: ')
    nazwaO = input('Nazwa obiektu: ')

    if nazwaI not in imprezy:
        print('Impreza o podanej nazwie nie istnieje!')
    else:
        if nazwaO not in obiekty:
            print('Obiekt o podanej nazwie nie istnieje!')
        else:
            o = obiekty[nazwaO]
            i = imprezy[nazwaI]
            if i.obiekt == "brak":
                i.dodajObiekt(o)
                o.dodajImpreze(i)
                print(f'{nazwaI} odbedzie sie w obiekcie {nazwaO}')
            else:
                print(f'Impreza już ma dodany obiekt o nazwie {i.obiekt.nazwa}!')


def fFunkcja():
    print("Dodajesz zespol do imprezy\n")
    nazwaI = input('Nazwa imprezy: ')
    nazwaZ = input('Nazwa zespolu: ')

    if nazwaI not in imprezy:
        print('Impreza o podanej nazwie nie istnieje!')
    else:
        if nazwaZ not in zespoly:
            print('Zespol o podanej nazwie nie istnieje!')
        else:
            i = imprezy[nazwaI]
            i.dodajZespol(zespoly[nazwaZ])
            print(f'{nazwaZ} zagra na imprezie {nazwaI}')


def gFunkcja():
    print("Dodajesz uczestnika do imprezy\n")
    nazwaI = input('Nazwa imprezy: ')
    nazwaU = input('Nazwa uczestnika: ')

    if nazwaI not in imprezy:
        print('Impreza o podanej nazwie nie istnieje!')
    else:
        if nazwaU not in uczestnicy:
            print('Uczestnik o pdanym loginie nie istnieje!')
        else:
            i = imprezy[nazwaI]
            u = uczestnicy[nazwaU]
            i.dodajUczestnika(u)
            print(f'{nazwaU} wezmie udzial w imprezie {nazwaI}')


def hFunkcja():
    print('Usuwasz obiekt\n')
    nazwa = input('Nazwa obiektu: ')

    if nazwa not in obiekty:
        print('Obiekt o podanej nazwie nie istnieje!')
    else:
        o = obiekty[nazwa]
        for i in imprezy:
            im = imprezy[i]
            if im.obiekt == o:
                im.usunObiekt()
        o.imprezki.clear()
        o.ile -= 1
        del obiekty[nazwa]
        print(f"Usunieto obiekt {nazwa} ")
        print(f"Zostalo jeszcze {Obiekt.policz()}")


def iFunkcja():
    print('Usuwasz impreze\n')
    nazwa = input('Nazwa imprezy: ')

    if nazwa not in imprezy:
        print('Impreza o podanej nazwie nie istnieje!')
    else:
        i = imprezy[nazwa]
        i.usunWszystko()
        i.usunObiekt()
        for o in obiekty:
            ob = obiekty[o]
            ob.usunImpreze(i)
        i.ile -= 1
        del imprezy[nazwa]
        print(f"Usunieto impreze {nazwa}")
        print(f"Zostalo jeszcze {Impreza.policz()}")


def jFunkcja():
    print('Usuwasz uczestnika\n')
    login = input('Login uczestnika: ')

    if login not in uczestnicy:
        print('Uczestnik o podanym loginie nie istnieje!')
    else:
        l = uczestnicy[login]
        for i in imprezy:
            im = imprezy[i]
            im.usunUczestnika(l)
        l.ile -= 1
        del uczestnicy[login]
        print(f"Usunieto uczestnika {login} ")
        print(f"Zostalo jeszcze {Uczestnik.policz()}")


def kFunkcja():
    print('Usuwasz zespol\n')
    nazwa = input('Nazwa zespolu: ')

    if nazwa not in zespoly:
        print('Zespol o podanej nazwie nie istnieje!')
    else:
        z = zespoly[nazwa]
        for i in imprezy:
            im = imprezy[i]
            im.usunZespol(z)

        z.ile -= 1
        del zespoly[nazwa]
        print(f"Usunieto uczestnika {nazwa} ")
        print(f"Zostalo jeszcze {Zespol.policz()}")


def lFunkcja():
    print(f'Wszystkie imprezy: {Impreza.policz()}\n')

    for i in imprezy:
        print(i)


def mFunkcja():
    print(f'Wszystkie obiekty: {Obiekt.policz()}\n')

    for o in obiekty:
        print(o)


def nFunkcja():
    print(f'Wszystkie zespoly: {Zespol.policz()}\n')

    for z in zespoly:
        print(z)


def oFunkcja():
    print(f'Wszyscy uczestnicy: {Uczestnik.policz()}\n')

    for u in uczestnicy:
        print(u)


def pFunkcja():
    print('Harmonogram imprezy\n')
    nazwa = input('Nazwa imprezy: ')

    if nazwa not in imprezy:
        print('Impreza o podanej nazwie nie istnieje!')
    else:
        i = imprezy.get(nazwa)
        i.wyswietlZespoly()


def rFunkcja():
    print('Uczestnicy imprezy\n')
    nazwa = input('Nazwa imprezy: ')

    if nazwa not in imprezy:
        print('Impreza o podanej nazwie nie istnieje!')
    else:
        i = imprezy.get(nazwa)
        i.wyswietlUczestnikow()


def sFunkcja():
    print('Obiekt, na ktorym odbedzie sie impreza\n')
    nazwa = input('Nazwa imprezy: ')

    if nazwa not in imprezy:
        print('Impreza o podanej nazwie nie istnieje!')
    else:
        i = imprezy.get(nazwa)
        print(i.obiekt)


def tFunkcja():
    print('Imprezy na obiekcie')
    nazwa = input('Nazwa obiektu: ')

    if nazwa not in obiekty:
        print('Obiekt o podanej nazwie nie istnieje!')
    else:
        o = obiekty.get(nazwa)
        o.wyswietlImprezy()


def uFunkcja():
    print('Do widzenia!')
    sys.exit()
