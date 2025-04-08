def lees_csv(bestandsnaam):
    resultaat = []
    try:
        with open(bestandsnaam, 'r') as bestand:
            for regel in bestand:
                waarden = regel.strip().split(',')
                resultaat.append(waarden)
        return resultaat
    except FileNotFoundError:
        print(f"Fout: Bestand '{bestandsnaam}' niet gevonden.")
        return []
    except Exception as e:
        print(f"Fout bij het lezen van het bestand: {e}")
        return []

def schrijf_csv(bestandsnaam, gegevens):
    try:
        with open(bestandsnaam, 'w') as bestand:
            for rij in gegevens:
                regel = ','.join(str(waarde) for waarde in rij)
                bestand.write(regel + '\n')
        print(f"Gegevens succesvol weggeschreven naar '{bestandsnaam}'")
        return True
    except Exception as e:
        print(f"Fout bij het schrijven naar het bestand: {e}")
        return False

def test_module():
    return "De CSV-module is succesvol geïmporteerd!"