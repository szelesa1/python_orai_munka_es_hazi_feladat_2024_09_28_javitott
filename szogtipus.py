"""
6. feladat – Szögtípus
A program  kérjen be a konzolról egy valós számot! Ha ez a szám 0 és 360 közé esik, akkor legyen egy szög mértéke (pl. 60 fok), egyébként a program adjon hibaüzenetet! Ha lehet, a program írja ki a szög mértéke alapján a szög típusát (pl.: 60 -> hegyesszög)!
"""

# nullszög = 0 fok
# hegyesszög = 0 foknál nagyobb, de 90 foknál kisebb.
# derékszög = 90 fok
# tompaszög = 90 foknál nagyobb, de 180 foknál kisebb.
# egyenesszög = 180 fok
# homorúszög = 180 foknál nagyobb, de 360 foknál kisebb.
# teljesszög = 360 fok

def szogtipus():
    fok = float(input("Kérem, adjon meg egy valós számot! "))
    if fok >= 0 and fok <= 360:
        print("A szög mértéke " + str(fok) + " fok.")
        if fok == 0:
            print("A megadott szám egy nullszög típus.")
        elif fok > 0 and fok < 90:
            print("A megadott szám egy hegyesszög típus.")
        elif fok == 90:
            print("A megadott szám egy derékszög típus.")
        elif fok > 91 and fok < 180:
            print("A megadott szám egy tompaszög típus.")
        elif fok == 180:
            print("A megadott szám egy egyenesszög típus.")
        elif fok > 181 and fok < 360:
            print("A megadott szám egy homorúszög típus.")
        elif fok == 360:
            print("A megadott szám egy teljesszög típus.")
    else:
        print("A szám nem esik 0 és 360 érték közé.")