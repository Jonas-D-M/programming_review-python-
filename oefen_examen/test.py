from models.Huisartspraktijk import Huisartspraktijk


def test():
    bestandsnaam = "oefen_examen\\bronbestand\huisartsen.csv"

    huisartspraktijken = Huisartspraktijk.inlezen_huisartsen(bestandsnaam)

    Huisartspraktijk.print_info_alle_praktijken(huisartspraktijken)

    praktijk = Huisartspraktijk.zoek_info_arts(huisartspraktijken,"vanacker")

    print(praktijk)

test()

def run():
    bestandsnaam = "oefen_examen\\bronbestand\huisartsen.csv"
    huisartspraktijken = Huisartspraktijk.inlezen_huisartsen(bestandsnaam)

    actie = input("\nKies uit volgende menu-items:\np = print lijst huisartspraktijken, z = laad zoekfuncties, v = verlaat programma:>")

    while actie!="v":
        if actie == "p":
            Huisartspraktijk.print_info_alle_praktijken(huisartspraktijken)
        elif actie == "z":
            naam_huisarts = input("Geef (een deel van) de naam van huisarts in:>")
            praktijk = Huisartspraktijk.zoek_info_arts(huisartspraktijken,naam_huisarts)
            print(praktijk)
        actie = input("\nKies uit volgende menu-items:\np = print lijst huisartspraktijken, z = laad zoekfuncties, v = verlaat programma:>")

run()




