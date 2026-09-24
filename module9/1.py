class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


# Pääohjelma
auto1 = Auto("ABC-123", 142)

print(f"Rekisteritunnus: {auto1.rekisteritunnus}")
print(f"Huippunopeus: {auto1.huippunopeus} km/h")
print(f"Nopeus: {auto1.nopeus} km/h")
print(f"Kuljettu matka: {auto1.matka} km")