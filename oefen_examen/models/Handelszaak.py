from models.Adres import Adres
from models.logger import handelszaak_properties_logger


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


    def __str__(self):
        return f'{super().__str__()}  telefoonnummer: {self.telefoonnummer}'


    def __eq__(self, other):
        if super().__eq__(other) and self.telefoonnummer == other.telfoonnummer:
            return True
        else:
            return False


    def __lt__ (self, other):
        if super().__lt__(other):
            return True
        else:
            return False