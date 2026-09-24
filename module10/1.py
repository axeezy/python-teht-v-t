class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi nousi kerrokseen {self.kerros}.")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi laski kerrokseen {self.kerros}.")

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylös()
        while self.kerros > kohde:
            self.kerros_alas()


h = Hissi(0, 10)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(h.alin_kerros)