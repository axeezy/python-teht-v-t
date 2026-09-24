import random

koodi3 = ""
for i in range(3):
    koodi3 += str(random.randint(0, 9))

koodi4 = ""
for i in range(4):
    koodi4 += str(random.randint(1, 6))

print(f"Kolminumeroinen koodi: {koodi3}")
print(f"Nelinumeroinen koodi: {koodi4}")