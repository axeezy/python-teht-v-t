viikonpaivat = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
jarjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpaiva = viikonpaivat[jarjestysnumero - 1]
print(f"{jarjestysnumero}. viikonpäivä on {viikonpaiva}.")