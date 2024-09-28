def minta_while2():
    n = 5
    m = int(input("Kérek egy számot: "))
    while n > m:
        n -= 1
        print("n = ",n) # Ha igaz, beljebb kezdődik, rögtön megtörténik a kiiratás, addig írja ki a számokat, amíg hamis nem lesz. Ha hamis, nem ír ki semmit.