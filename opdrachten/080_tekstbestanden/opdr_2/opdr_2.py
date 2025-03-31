# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)
print(geheim_getal)
# De rest moet jij doen.....

print("Raad een getal tussen 1 en 100")
pogingen = 0

while True:
    gok = int(input("Jouw gok: "))
    pogingen += 1

    if gok < geheim_getal:
        print("Te laag")
    elif gok > geheim_getal:
        print("Te hoog")
    else:
        print(f"Juist geraden, het getal was {geheim_getal}")
        print(f"Je hebt {pogingen} gedaan om het juist antwoord te krijgen")
        break
