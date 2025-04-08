# Opdracht 1 functies
# Naam student:
# Groep:

# importeer de module csv...

# Importeer de zelfgemaakte module
from my_modules.csv import schrijf_csv, test_module

def main():

    print(test_module())
    
    studenten = [
        ["ID", "Naam", "Leeftijd", "Studierichting"],
        ["1", "Emma de Vries", "21", "Informatica"],
        ["2", "Thomas Bakker", "19", "Economie"],
        ["3", "Sophie Janssen", "22", "Geneeskunde"],
        ["4", "Lucas van Dijk", "20", "Werktuigbouwkunde"],
        ["5", "Bjorn Koerhuis", "26", "ICT"]
    ]
    
    bestandsnaam = "studenten.csv"
    schrijf_csv(bestandsnaam, studenten)

if __name__ == "__main__":
    main()