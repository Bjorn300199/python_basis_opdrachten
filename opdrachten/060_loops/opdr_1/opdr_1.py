# Opdracht 1 loops
# Naam student:
# Groep:

# Maak een loop waarin je een lijst vult met de getallen van 1 t/m 10. Print de lijst op het scherm.

# Hier start de for-loop....

my_list = []

for i in range(10):
    cijfer = input(f"Cijfer {i}: ")
    my_list.append(cijfer)

print("Cijfers van 1 tot 10 in een list.")
print(my_list)