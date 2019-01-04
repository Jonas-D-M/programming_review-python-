from models.Adres import Adres
from logger import handelszaak_properties_logger


class Handelszaak(Adres):


    def __init__(self,straat, huisnummer : int, postcode : int, gemeente, telefoonnummer):
        Adres.__init__(self, straat, huisnummer, postcode, gemeente)
        self.telefoonnummer = telefoonnummer


    @property
    def telefoonnummer(self):
        return self.__telefoonnummer

    @telefoonnummer.setter
    def telefoonnummer(self, value):
        if isinstance(value, str):
            self.__telefoonnummer = value
        else:
            handelszaak_properties_logger.error('Telefoonnummer has to be a string.')