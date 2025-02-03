"""
2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt,
amely True értékkel tér vissza, ha a paraméterként átvett listaelemek (egész számok) között van páros,
ellenkező esetben a visszatérési érték False! A program tartalmazza a függvény hívását is!
"""

def paros_e(listaelemek):
    for elem in listaelemek:
        if elem % 2 != 0:
            return True
    return False


print(f"A listában van páros szám: {paros_e([1, 8, 17, 22, 40])}")