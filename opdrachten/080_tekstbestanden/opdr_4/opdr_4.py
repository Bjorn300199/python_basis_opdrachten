# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Welk eten neem je mee?",
    "Welke drank neem je mee?"
]

alle_gasten = []

meer_gasten = True
while meer_gasten:
    print("Vul de onderstaande lijst in om je in te schrijven")

    gast_info = {}

    for i, vraag in enumerate(vragen, 1):
        print(f"{i}. {vraag}")
        antwoord = input("> ")

        if i == 1:
            gast_info["voornaam"] = antwoord
        elif i == 2:
            gast_info["achternaam"] = antwoord
        elif i == 3:
            gast_info["eten"] = antwoord
        elif i == 4:
            gast_info["drank"] = antwoord

alle_gasten.append(gast_info)

bestandsnaam = "gastenlijst.txt"

with open(bestandsnaam, "w") as bestand:
    for i, gast in enumerate(alle_gasten, 1):
        bestand.write(f"gast {i}.\n")
        bestand.write(f"Voonaam: {gast['voornaam']} {gast['achternaam']}\n")
        bestand.write(f"Eten: {gast['eten']}\n")
        bestand.write(f"Drank: {gast['drank']}\n") 