"""
5. Feladat
Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír!
A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvények, amely
a lista legkisebb elemével tér vissza. A program írja ki, hogy melyik volt a megadott legkisebb szám!
"""

def smallest(listaelemek):
    min = listaelemek[0]
    for elem in listaelemek:
        if elem < min:
            min = elem
    return min

listaelemek = []

while True:
    szam = int(input("Adjon meg egy számot: "))
    if szam == 0:
        break
    listaelemek.append(szam)

print(f"A legkisebb szám: {smallest(listaelemek)}")
