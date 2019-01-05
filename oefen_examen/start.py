from models.Huisartspraktijk import Huisartspraktijk


def test():
    #inlezen bestand
    fp= 'oefen_examen\\bronbestand\huisartsen.csv'
    list_praktijken = Huisartspraktijk.inlezen_huisartsen(fp)
    Huisartspraktijk.print_info_alle_praktijken(list_praktijken)

    #zoeken van arts
    praktijk = Huisartspraktijk.zoek_info_arts(list_praktijken, 'vanacker')
    print(praktijk)

# test()


def run():
    fp = 'oefen_examen\\bronbestand\huisartsen.csv'
    list_praktijken = Huisartspraktijk.inlezen_huisartsen(fp)
    while True:
        print('What would you like to do:\n1)print alle praktijken: p\nEen arts zoeken: z\nVerlaten: v\n')
        response = input()
        if response == 'p':
            Huisartspraktijk.print_info_alle_praktijken(list_praktijken)
        elif response == 'z':
            print('Geef de naam op van de arts die u wenst te vinden:\n')
            response2 = input()
            found = Huisartspraktijk.zoek_info_arts(list_praktijken, response2)
            Huisartspraktijk.print_info_alle_praktijken(found)
        elif response == 'v':
            break


run()
