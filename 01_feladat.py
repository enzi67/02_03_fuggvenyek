"""
1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett
listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! A program tartalmazza a
függvény hívását is!
"""

def osszegzo(listaelemek):
    osszeg = 0
    for elem in listaelemek:
        osszeg += elem
    return osszeg  

print(f"A számok összege: {osszegzo([1, 5, 9, 13, 29])}.")