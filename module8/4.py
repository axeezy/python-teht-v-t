import random

def heitä():
    eka, toka = random.randint(1, 6), random.randint(1, 6)
    return eka, toka

noppa1, noppa2 = heitä()
print(f"Nopista tuli {noppa1} ja {noppa2}.")