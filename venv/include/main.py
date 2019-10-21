import sys
from funkcje import aFunkcja, bFunkcja, cFunkcja, dFunkcja, eFunkcja, fFunkcja, gFunkcja, hFunkcja, iFunkcja, jFunkcja,\
    kFunkcja, lFunkcja, mFunkcja, nFunkcja, oFunkcja, pFunkcja, rFunkcja, sFunkcja, tFunkcja, uFunkcja
from os import system, name

def screen_clear():
   if name == 'nt':
      _ = system('cls')
   else:
      _ = system('clear')

switcher = {
        1: aFunkcja,
        2: bFunkcja,
        3: cFunkcja,
        4: dFunkcja,
        5: eFunkcja,
        6: fFunkcja,
        7: gFunkcja,
        8: hFunkcja,
        9: iFunkcja,
        10: jFunkcja,
        11: kFunkcja,
        12: lFunkcja,
        13: mFunkcja,
        14: nFunkcja,
        15: oFunkcja,
        16: pFunkcja,
        17: rFunkcja,
        18: sFunkcja,
        19: tFunkcja,
        20: uFunkcja,
    }

def switch(char):

    func = switcher.get(char, lambda: print("Nie ma takiej opcji w menu"))
    return func()

while(True):
    print("========================= System imprezowy ==========================\n")
    print("Autor: Anna Cielas\n")
    print("=====================================================================")
    print('MENU GLOWNE')
    print("1. Dodaj Obiekt")
    print("2. Dodaj Impreze")
    print("3. Dodaj Uczestnika")
    print("4. Dodaj Zespol")
    print("5. Dodaj Impreze do Obiektu")
    print("6. Dodaj Zespol do Imprezy")
    print("7. Dodaj Uczestnika do Imprezy")
    print("8. Usun Obiekt")
    print("9. Usun Impreze")
    print("10. Usun Uczestnika")
    print("11. Usun Zespol")
    print("12. Wyswietl wszystkie Imprezy")
    print("13. Wyswietl wszystkie Obiekty")
    print("14. Wyswietl wszystkie Zespoly")
    print("15. Wyswietl wszystkich Uczestników")
    print("16. Wyswietl harmonogram Imprezy")
    print("17. Wyswietl uczestnikow Imprezy")
    print("18. Wyswietl miejsce Imprezy")
    print("19. Wyswietl imprezy na Obiekcie")
    print("20. Koniec programu")

    wybor = int(input('\nWybierz modul: ').strip())
    switch(wybor)
    input("Nacisnij enter, aby wrocic do menu")
    print('\n\n\n\n\n\n\n\n\n\n\n\n')
    continue





