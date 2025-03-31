# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

vraag1 = input("Wat vind je van de huidige regering? ")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe? ")
vraag3 = input("Wat vind jij de mooiste stad van Nederland? ")

print(f"Wat vind je van de huidige regering? {vraag1}")
print(f"Wat vind je van de Python-lessen tot nu toe? {vraag2}")
print(f"Wat vind jij de mooiste stad van Nederland? {vraag3}")

with open("enquete.txt", "a") as bestand:
    bestand.write("Enquete Antwoorden\n")
    bestand.write(f"Vraag1: {vraag1}\n")
    bestand.write(f"Vraag2: {vraag2}\n")
    bestand.write(f"Vraag3: {vraag3}\n")