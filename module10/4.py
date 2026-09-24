import random


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

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit


class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\n--- {self.nimi}: tilanne ---")
        print(f"{'Rekisteritunnus':<15}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
        for auto in self.autot:
            print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<15}{auto.nopeus:<10}{round(auto.matka, 1):<10}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False


autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunteja = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunteja += 1
    if tunteja % 10 == 0:
        kilpailu.tulosta_tilanne()

kilpailu.tulosta_tilanne()