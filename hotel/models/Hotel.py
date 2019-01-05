from models.logger import hotel_properties_logger
from models.Hotelkamer import Hotelkamer


class Hotel():


    def __init__(self):
        self.__kamers_dict = {}


    @property
    def kamer_dict(self):
        return self.__kamers_dict

    @kamer_dict.setter
    def kamer_dict(self, value):
        if isinstance(value, Hotelkamer):
            self.__kamers_dict.update({value.kamernummer : value.gasten_lijst})
        else:
            hotel_properties_logger.error('Only objects of the class hotelkamer can be added to the dictionary')


    def voeg_kamers_toe(self,kamer):
        if isinstance(kamer, Hotelkamer):
            self.__kamers_dict.update({kamer.kamernummer : kamer.gastenlijst})
        else:
            hotel_properties_logger.error('not an object of the class Hotelkamer')


    def print_alle_vrije_kamers(self):
        vrije_kamers = []
        for k,v in self.__kamers_dict.items():
            if len(v) == 0:
                vrije_kamers.append(k)
        return vrije_kamers


    def print_alle_bezette_kamers(self):
        bezette_kamers = []
        for k,v in self.__kamers_dict.items():
            if len(v) > 0:
                bezette_kamers.append(i)
        return bezette_kamers


    def reservatie_maken(self, kamer_nummer, gasten):
        if len(self.__kamers_dict[kamer_nummer]) == 0:
            for i in gasten:
                self.kamer_dict[kamer_nummer].append(i)
            hotel_properties_logger.info(f'Een reservatie werd gemaakt voor {gasten} in kamer {kamer_nummer}')
        else:
            hotel_properties_logger.info(f'Kamer {kamer_nummer} is reeds bezet.')


    def reservatie_zoeken(self, gast):
        counter = 0
        for k,v in self.__kamers_dict.items():
            for i in v:
                if gast.lower() in i.naam.lower() or gast.lower() in i.voornaam.lower():
                    print(f'{gast} verblijft in kamer nummer {k}')
                    counter += 1
        if counter == 0:
            print('Deze gast kon niet worden gevonden')


    def toon_kamerbezetting(self, kamernummer):
        if isinstance(kamernummer, int):
            for k,v in self.__kamers_dict.items():
                if k == kamernummer:
                    for i in v:
                        print(i)
        else:
            hotel_properties_logger.error('De input voor toon_kamerbezetting was geen int.')


    def info_kamer(self, kamernummer):
        counter = 0
        if isinstance(kamernummer, int):
            for k,v in self.__kamers_dict.items():
                if k == kamernummer:
                    print(f'kamer {kamernummer} heeft de volgende gasten:')
                    for i in v:
                        print(i)
                    counter += 1
            if counter == 0:
                print('Het kamer nummer dat u opgaf bestaat niet.')
        else:
            hotel_properties_logger.error('De input voor info kamer was geen int.')




