def egy_a():
    for i in range(-6):
        print(i, end=" ")


def egy_b():
    for i in range(16, 6):
        print(i, end=" ")


def egy_c():
    for i in range(16, 6, -2):
        print(i, end=" ")


def harom():
    # 1. megoldás
    for i in range(0, 21):
        print(i, end=" ")

    # 2. megoldás, for i in range(0,21,1):
    for i in range(21):
        print(i, end=" ")

    # 3. megoldás
    for i in range(0, 21, 1):
        print(i, end=" ")

    # 4. megoldás
    i = 0
    while i < 21:
        print(i)
        i += 1


def negy():
    for i in range(20, 57, 2):
        print(i, end=" ")


def ot():
    for i in range(77, -77, -4):
        print(i, end=" ")


def beolvas():
    szam = int(input("Kérem adjon meg egy egész számot! "))
    return szam


def hat():
    szam1 = beolvas()
    szam2 = beolvas()

    # melyik a nagyobb
    if szam2 < szam1:
        # csere
        atmenet = szam1
        szam1 = szam2
        szam2 = atmenet

    for i in range(szam1, szam2+1, 1):
        print(i, end=" ")


def het():
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    if szorzat < 0:
        for i in range(0, szorzat-1, -1):
            print(i, end=" ")
    else:
        for i in range(0, szorzat+1, 1):
            print(i, end=" ")


def nyolc():
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    while
        for i in range(0, szorzat + 1)