import logging

from models.Bier import Bier


# DEMO test-methode

def instellen_log():
    logging.basicConfig(filename='logging_bieren.txt', level=logging.DEBUG,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def print_bieren(lijst_bieren):
    for bier in lijst_bieren:
        print("%s -> alcoholpercentage: %s" % (bier, bier.alcoholpercentage))


def oefening_bieren():
    lijst_bieren = Bier.inlezen_bieren()
    lijst_bieren.sort()

    actie = input(
        "Geef opdracht door:\n 'p' om alle ingelezen bieren af te printen,\n 'n' om een bier op basis van een deel van de naam op te zoeken,\n 'a' om alle bieren tussen 2 alcoholpercentages af te printen,\n 'b' om de bieren uit een specifieke brouwerij af te printen, \n 'x' om te stoppen>:")
    while (actie != 'x'):
        if (actie == 'p'):
            print_bieren(lijst_bieren)
        if (actie == 'n'):
            zoek = input(">>>Geef deel van naam van bier op: ")
            print("Gevonden resultaten zijn: ")
            resultaat = Bier.zoek_bieren_op_naam(lijst_bieren, zoek)
            print_bieren(resultaat)
        if (actie == 'a'):
            min_percentage = float(input(">>>Geef het minimum alcohol percentage op: "))
            max_percentage = float(input(">>>Geef het maximum alcohol percentage op: "))
            print("Gevonden bieren binnen deze marge zijn: ")
            resultaat = Bier.zoek_bieren_op_alcoholpercentage(lijst_bieren, min_percentage, max_percentage)
            print_bieren(resultaat)
        actie = input(
            "Geef opdracht door:\n 'p' om alle ingelezen bieren af te printen,\n 'n' om een bier op basis van een deel van de naam op te zoeken,\n 'a' om alle bieren tussen 2 alcoholpercentages af te printen,\n 'x' om te stoppen>:")


# instellen_log()
oefening_bieren()
