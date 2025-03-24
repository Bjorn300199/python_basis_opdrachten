# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
print(rivieren[0])
print(rivier_info["rijn"][1])
 
# Heb dit met ChatGPT gedaan. Het is wel duidelijk, rivier = "rijn" Haalt informatie uit de lijst "rijn".
# land = rivier_info kijkt naar het land in de variable van rij 21 en pakt vervolgens het land dmv het nummer tussen brackets 
# # De print pakt eerst de rivier in lijn 22, maakt daar de eerste letter een hoofdletter, dit ook bij land.
# Weet niet waarom capatalize() met () moet eindigen.
rivier = "rijn"
land = rivier_info[rivier][1]
print(f"De rivier {rivier.capitalize()} stroomt onder andere door {land.capitalize()}")