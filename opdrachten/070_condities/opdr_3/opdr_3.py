# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...
while True:
    age = int(input("Please enter your age: "))

    catagory = None

    for cat, (min_age, max_age) in leeftijd.items():
        if age >= min_age and age <= max_age:
            catagory = cat
            break
            
    if catagory is not None:
        discount = kortings_percentages[catagory]
        discountedprice = normale_toegangsprijs * (1 - discount / 100)
        print(f"Your price: {discountedprice}")
        break
    else:
        print("Enter a valid age")
