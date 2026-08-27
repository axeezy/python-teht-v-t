print("Anna leiviskät.")
leiviskat = float(input())
print()

print("Anna naulat.")
naulat = float(input())
print()

print("Anna luodit.")
luodit = float(input())
print()

naulat_yhteensa = leiviskat * 20 + naulat
luodit_yhteensa = naulat_yhteensa * 32 + luodit
grammat_yhteensa = luodit_yhteensa * 13.3

kilot = int(grammat_yhteensa // 1000)
grammat = grammat_yhteensa - kilot * 1000

print("Massa nykymittojen mukaan:")
print(f"{kilot} kilogrammaa ja {grammat:.2f} grammaa.")