# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

landen = []

for i in range(5):
    land = input(f"Land {i+1}:")
    landen.append(land)

landen.sort(reverse=True)

print("Lijst met Landen:")
print(landen)