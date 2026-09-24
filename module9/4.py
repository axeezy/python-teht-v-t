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


autot = []
for i in range(1, 11):
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)
        if auto.matka >= 10000:
            kilpailu_kaynnissa = False

print(f"{'Rekisteritunnus':<15}{'Huippunopeus':<15}{'Nopeus':<10}{'Matka':<10}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<15}{auto.nopeus:<10}{round(auto.matka, 1):<10}")