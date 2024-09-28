"""
15. feladat – Téglalap1
A program olvasson be a konzolról két valós számot! Ha mindkét szám pozitív, akkor legyenek a beolvasott számok egy téglalap oldalai. A program számítsa ki a téglalap kerületét, területét, és írja ki két tizedesre kerekítve az eredményeket a konzolra! Hiba esetén írja ki: "Hiba: a téglalap oldalai nem pozitívak!"!
"""
# a téglalap kerülete: 2 × (a + b)
# a téglalap területe: a × b

def teglalap1():
    a = float(input("Kérem adjon meg egy pozitív valós számot! "))
    b = float(input("Kérem adjon meg még egy pozitív valós számot! "))
    eredmeny_kerulet = round(2 * (a + b), 2)
    eredmeny_terulet = round((a * b), 2)
    if a > 0 and b > 0:
        print("Ezek lettek a téglalap a és b oldalai.")
        if eredmeny_kerulet > 0 and eredmeny_terulet > 0:
            print("A téglalap kerülete: " + str(eredmeny_kerulet)) #ide is beírható a round függvény
            print("A téglalap területe: " + str(eredmeny_terulet)) #ide is beírható a round függvény
    else:
        print("Hiba: a téglalap oldalai nem pozitívak!")

"""
kettő "#" neve együtt metódus

# ez nem egy eljárás, ez egy függvény
def egesz_beolvas():
    szam = float(input("Kérem adjon meg egy pozitív valós számot! "))
    return szam
    
# eljárás
def teglalap(): <- a main.py fájlnál ezt hívom meg
    oldal1 = egesz_beolvas()
    oldal2 = egesz_beolvas()
    
    if (oldal1) > 0 and (oldal2) > 0:
        kerulet = 2 * (oldal1 + oldal2)
        terulet = oldal1 * oldal2
        print("A téglalap kerülete: "+str(kerulet)+", területe: "+str(terulet)
    else:
        print("Hiba: a téglalap oldalai nem pozitívak!")
"""
