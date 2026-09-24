def tervehdi(tervehdys="Hei", kerrat=1):
    for i in range(kerrat):
        print(tervehdys + " " + str(i+1) + ". kerran")
    return

tervehdi()
tervehdi("Terve", 3)
tervehdi(kerrat=2, tervehdys="Moro")