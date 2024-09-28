"""
14. feladat – Kocka
A program olvasson be a konzolról egy egész számot! Ha a szám pozitív, akkor legyen a beolvasott szám egy kocka élének hossza. A program számítsa ki és írja ki a kocka felszínét, térfogatát a konzolra! Ha a szám nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kocka élének hossza nem pozitív!"!
"""

# a kocka térfogata: V = a3
# a kocka felszíne: A = 6 × a2

def kocka():
    a = int(input("Kérem, adja meg a kocka élének hosszát! "))
    eredmeny_terfogat = round((a ** 3), 2) #pow(el, 3)
    eredmeny_felszin = round((6 * a **2), 2)
    if eredmeny_terfogat >= 0 and eredmeny_felszin >= 0:
        print("A kocka térfogata: " + str(eredmeny_terfogat))
        print("A kocka felszíne: " + str(eredmeny_felszin))
    else:
        eredmeny_terfogat < 0 and eredmeny_felszin < 0
        print("Hiba: a kocka élének hossza nem pozitív!")