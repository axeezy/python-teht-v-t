nimet    = []

nimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
nimet.append(nimi)
while nimi != "":
    valinta = input ("haluatko lis't' vai poistaa (1 tai p)") 
    nimet.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")
    nimet.remove ("alex")
print(nimet)