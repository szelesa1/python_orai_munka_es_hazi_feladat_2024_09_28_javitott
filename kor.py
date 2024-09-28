"""
13. feladat – Kör
A program olvassa be a konzolról egy kör sugarát! Ha a sugár nem pozitív, akkor a program írja ki konzolra, hogy "Hiba: a kör sugara nem pozitív!"; egyébként a program számítsa ki és írja ki a kör kerületét, területét a konzolra!
"""

# kör terület számítása: 2 × r × pí
# kör terület képlete: r2 × pí

import math


def kor():
    kor_sugara = float(input("Kérem, adja meg egy kör sugár értéket! "))
    eredmeny_kerulet = round(2 * kor_sugara * math.pi, 2)
    eredmeny_terulet = round(kor_sugara ** 2 * math.pi, 2) #r * r * math.pi vagy math.pow(r, _y:2) * math.pi vagy pow(r, 2) * math.pi
    if eredmeny_kerulet > 0 and eredmeny_terulet > 0:
        print("A kör kerülete: " + str(eredmeny_kerulet))
        print("A kör területe: " + str(eredmeny_terulet))
    else:
        eredmeny_kerulet < 0 and eredmeny_terulet < 0
        print("Hiba: a kör sugara nem pozitív!")

"""
Nem túl bonyolítva:
r = float(input("Kérem, adja meg egy kör sugár értéket! "))
    if r>0:
        terulet = r ** 2 * math.pi
        kerulet = 2 * r * math.pi
        
        print("A kör területe: "+str(terulet)+", a kör kerülete: "+str(kerulet)+".")
    else:
        print("Hiba: a kör sugara nem pozitív!")
"""