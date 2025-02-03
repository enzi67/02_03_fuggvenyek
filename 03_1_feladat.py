"""
3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként
átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza!
A program tartalmazza a függvény hívását is!
"""

def dev_by_three(listaelemek):
    count = 0
    for elem in listaelemek:
        if elem % 3 == 0:
            count += 1
    return count


print(f"A listában {dev_by_three([1, 5, 9, 13, 42])} hárommal osztható szám van.")