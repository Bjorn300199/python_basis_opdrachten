# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

my_list = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']
my_list.sort()
my_list.append("Peperoni")
my_list.remove("verdi")

print(my_list[0:3])

middle = len(my_list) // 2
middlevalue = my_list[middle]
print(f"Middle value is: {middlevalue}")

print(my_list[2:5])
print(my_list)