"""
7. feladat – Négyzetgyök
A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!
"""
import math


def negyzetgyok():
    szam = float(input("Kérem, adjon meg egy számot! "))
    if szam >= 0:
        gyok = math.sqrt(szam)
        print(gyok)
    else:
        print("HIBA: negatív szám gyökét akarja számolni!")

"""
helytelen megoldás:

szam1 = float(input("Kérem, adjon meg egy valós számot! "))
szam2 = float(input("Kérem, adja meg a hatvány értékét! "))
eredmeny = szam1 ** szam2
if szam1 >= 0 and szam2 >= 0:
    print("A két szám négyzetgyöke " + str(eredmeny))
else:
    print("Hiba! Negatív szám nem adható meg!")
"""