"""
3.2 Feladat
Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a
program egy listában, és ezt értékelje ki a függvény! (Az adatbeolvasás addig tartson, míg a
felhasználó negatív számot nem ad meg!)
"""

def dev_by_3_osszegzo(listaelemek):
    osszeg = 0
    for elem in listaelemek:
        if elem % 3 == 0:
            osszeg += 1
    return osszeg

listaelemek = []

while True:
    szam = int(input("Adjon meg egy számot: "))
    if szam == 0:
        break
    listaelemek.append(szam)

print(f"A listában {dev_by_3_osszegzo(listaelemek)} hárommal osztható szám van.")