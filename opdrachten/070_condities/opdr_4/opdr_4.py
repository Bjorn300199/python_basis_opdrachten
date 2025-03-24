# Opdracht 4 condities
# Naam student:
# Groep:


toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = [toppingname[0] for toppingname in toppings]

while True:
    keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

    price = 0
    found = False

    for toppingname, toppingprice in toppings:
        if keuze == toppingname:
            price = toppingprice
            found = True
            break

    if found == True:
        print(f"The price of {keuze} is: €{price:.2f}")
        break
    else:
        print("Give a valid topping")