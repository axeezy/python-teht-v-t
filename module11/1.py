class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}")
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}")
        print(f"Päätoimittaja: {self.päätoimittaja}")


aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti_no6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
print()
hytti_no6.tulosta_tiedot()