# Luodaan lista nimeltä 'autot'
autot = [
    # Ensimmäinen auto (sanakirja)
    {
        "merkki": "Toyota",
        "malli": "Corolla",
        "vuosimalli": 2018
    },
    # Toinen auto (sanakirja)
    {
        "merkki": "Ford",
        "malli": "Focus",
        "vuosimalli": 2020
    },
    # Kolmas auto (sanakirja)
    {
        "merkki": "VW",
        "malli": "ID.3",
        "vuosimalli": 2023
    }
]

print(autot[2] ["merkki"], autot[2]["malli"], autot[2]["vuosimalli"])
for auto in autot:
    print(auto["merkki"],auto["malli"],auto["vuosimalli"])
    print(f"Merkki: {auto['merkki']}, Malli: {auto['malli']}, Vuosimalli: {auto['vuosimalli']}")


lista = [(1,2,3),(4,5,6),(7,8,9)]
print(lista)