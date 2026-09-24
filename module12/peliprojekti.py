class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino


class Huone:
    def __init__(self, nimi, esine=None):
        self.nimi = nimi
        self.esine = esine


class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, kohde):
        self.sijainti = kohde
        print(f"{self.nimi} siirtyi huoneeseen {kohde.nimi}.")

    def keraa_esine(self):
        if self.sijainti.esine is not None:
            esine = self.sijainti.esine
            self.esineet.append(esine)
            self.sijainti.esine = None
            print(f"{self.nimi} keräsi esineen {esine.nimi}.")
        else:
            print("Täällä ei ole esinettä kerättäväksi.")


def lue_tiedosto(tiedostonimi):
    with open(tiedostonimi, "r", encoding="utf-8") as f:
        print(f.read())


def tallenna_peli(pelaaja):
    with open("tallennus.txt", "w", encoding="utf-8") as f:
        f.write(f"{pelaaja.nimi}\n")
        f.write(f"{pelaaja.sijainti.nimi}\n")
    print("Peli tallennettu.")


def lataa_peli(huoneet):
    try:
        with open("tallennus.txt", "r", encoding="utf-8") as f:
            rivit = f.read().splitlines()
            nimi = rivit[0]
            sijainnin_nimi = rivit[1]

            for huone in huoneet:
                if huone.nimi == sijainnin_nimi:
                    print(f"Tervetuloa takaisin, {nimi}!")
                    return Pelaaja(nimi, huone)

    except FileNotFoundError:
        return None


lue_tiedosto("intro.txt")
lue_tiedosto("ohjeet.txt")

miekka = Esine("Miekka", 2.5)
avain = Esine("Avain", 0.1)

eteinen = Huone("Eteinen")
kirjasto = Huone("Kirjasto", miekka)
kellari = Huone("Kellari", avain)

huoneet = [eteinen, kirjasto, kellari]

pelaaja = lataa_peli(huoneet)
if pelaaja is None:
    nimi = input("Syötä nimesi: ")
    pelaaja = Pelaaja(nimi, eteinen)

while True:
    print(f"\nOlet huoneessa: {pelaaja.sijainti.nimi}")
    print("1. Liiku kirjastoon")
    print("2. Liiku kellariin")
    print("3. Liiku eteiseen")
    print("4. Kerää esine")
    print("5. Tallenna peli")
    print("6. Lopeta")

    valinta = input("Valintasi: ")

    if valinta == "1":
        pelaaja.liiku(kirjasto)
    elif valinta == "2":
        pelaaja.liiku(kellari)
    elif valinta == "3":
        pelaaja.liiku(eteinen)
    elif valinta == "4":
        pelaaja.keraa_esine()
    elif valinta == "5":
        tallenna_peli(pelaaja)
    elif valinta == "6":
        print("Peli lopetettu.")
        break
    else:
        print("Virheellinen valinta.")