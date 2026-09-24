def summa(*luvut):
    s = 0
    for l in luvut:
        s += l
    return s

print("Summa on", summa(1, 2, 3))