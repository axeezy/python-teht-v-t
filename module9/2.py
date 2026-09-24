class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0


auto1 = Auto("ABC-123", 142)

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
print(f"Nopeus: {auto1.nopeus} km/h")

auto1.kiihdytä(-200)
print(f"Nopeus hätäjarrutuksen jälkeen: {auto1.nopeus} km/h")