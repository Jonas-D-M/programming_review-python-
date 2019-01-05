from models.Hotelgast import Hotelgast
from models.Hotelkamer import Hotelkamer
from models.Hotel import Hotel

def kamers_aanmaken(aantal):
    list_kamers = []
    if isinstance(aantal, int):
        for i in range(1,aantal+1):
            kamer = Hotelkamer(i)
            list_kamers.append(kamer)
    else:
        print('input needs to be an int')
    return list_kamers


def run():
    kamers = kamers_aanmaken(10)
    hotel = Hotel()
    for i in kamers:
        hotel.voeg_kamers_toe(i)
    while True:
        response = input('Wat wenst u te doen:\n1) print alle vrije kamers: p\ninfo specifieke hotelkamer: i\nreservatie maken: r\nreservatie zoeken: z\nkamerbezetting tonen: k\nexit: x\n')
        if response == 'p':
            vrije_kamers = hotel.print_alle_vrije_kamers()
            for i in vrije_kamers:
                print(i)
        elif response == 'i':
            try:
                response2 = int(input('Geef het kamer nummer op:\n'))
                hotel.info_kamer(response2)
            except ValueError:
                print('U dient hier een int op te geven.')
        elif response == 'r':
            try:
                response3 = int(input('Geef het aantal gasten op die u wilt toevoegen.\n'))
                lijst_gasten = []
                for i in range(1, response3 + 1):
                    naam = input(f'geef de achternaam op van gast nummer {i}')
                    voornaam = input(f'geef de voornaam op van gast nummer {i}')
                    adres = input(f'geef het adres op van gast nummer {i}')
                    gast = Hotelgast(naam, voornaam, adres)
                    lijst_gasten.append(gast)
                    while True:
                        try:
                            kamernummer = int(input('geeft het gewenste kamer nummer op: '))
                            vrije_kamers = hotel.print_alle_vrije_kamers()
                            if kamernummer in vrije_kamers:
                                hotel.reservatie_maken(kamernummer, lijst_gasten)
                                print(f'Een reservatie werd gemaakt voor kamer nummer {kamernummer}, volgende gasten werden toegevoegd:')
                                for i in lijst_gasten:
                                    print(i)
                                break
                            else:
                                print('De kamer die u opgaf is al bezet of bestaat niet')
                        except ValueError:
                            print('U dient hier een int op te geven.')
            except ValueError:
                print('U dient hier een int op te geven.')
        elif response == 'z':
            response4 = input('Geef de naam op van de hotelgast die u wenst te vinden\n')
            hotel.reservatie_zoeken(response4)
        elif response == 'k':
            try:
                response5 = int(input('Geef het kamernummer op waarvan u de bezetting wenst te zien\n'))
                hotel.toon_kamerbezetting(response5)
            except ValueError:
                print('U dient hier een int op te geven.')
        elif response == 'x':
            break
        else:
            print('Geen geldig commando')

run()