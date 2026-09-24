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


class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, tankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.tankin_koko = tankin_koko


sähköauto = Sähköauto("ABC-15", 180, 52.5)
polttoauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdytä(100)
polttoauto.kiihdytä(90)

sähköauto.kulje(3)
polttoauto.kulje(3)

print(f"Sähköauto {sähköauto.rekisteritunnus} matkamittari: {sähköauto.matka} km")
print(f"Polttomoottoriauto {polttoauto.rekisteritunnus} matkamittari: {polttoauto.matka} km")