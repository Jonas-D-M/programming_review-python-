from models.Handelszaak import Handelszaak
from models.logger import huisartspraktijk_properties_logger


class Huisartspraktijk(Handelszaak):


    def __init__(self, straat, huisnummer, postcode, gemeente, telefoonnummer, praktijktype):
        Handelszaak.__init__(self, straat, huisnummer, postcode, gemeente, telefoonnummer)
        self.praktijktype = praktijktype


    @property
    def praktijktype(self):
        return self.__praktijktype

    @praktijktype.setter
    def praktijktype(self, value):
        if isinstance(value, str):
            self.__praktijktype = value
        else:
            huisartspraktijk_properties_logger.error('praktijktype needs to be a string.')

