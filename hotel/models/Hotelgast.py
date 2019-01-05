from models.logger import hotelgast_properties_logger


class Hotelgast():


    def __init__(self, naam, voornaam, adres):
        self.naam = naam
        self.voornaam = voornaam
        self.adres = adres


    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        if isinstance(value, str):
            self.__naam = value
        else:
            hotelgast_properties_logger.error('Naam needs to be a string')


    @property
    def voornaam(self):
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value):
        if isinstance(value, str):
            self.__voornaam = value
        else:
            hotelgast_properties_logger.error('voornaam needs to be a string')


    @property
    def adres(self):
        return self.__adres

    @adres.setter
    def adres(self, value):
        if isinstance(value, str):
            self.__adres = value
        else:
            hotelgast_properties_logger.error('adres needs to be a string')

