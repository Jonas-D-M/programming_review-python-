from models.Handelszaak import Handelszaak
from models.logger import huisartspraktijk_properties_logger


class Huisartspraktijk(Handelszaak):


    def __init__(self, straat, huisnummer, postcode, gemeente, telefoonnummer, praktijktype):
        Handelszaak.__init__(self, straat, huisnummer, postcode, gemeente, telefoonnummer)
        self.praktijktype = praktijktype
        self.__list_huisartsen = []


    @property
    def praktijktype(self):
        return self.__praktijktype

    @praktijktype.setter
    def praktijktype(self, value):
        if isinstance(value, str):
            self.__praktijktype = value
        else:
            huisartspraktijk_properties_logger.error('praktijktype needs to be a string.')


    @property
    def list_huisartsen(self):
        return self.__list_huisartsen
    
    @list_huisartsen.setter
    def list_huisartsen(self, value):
        if isinstance(value, str):
            self.__list_huisartsen.append(value)
        else:
            huisartspraktijk_properties_logger.error('huisarts needs to be a string')

    def __str__(self):
        return f'{super().__str__()}  praktijktype: {self.praktijktype} heeft de volgende huisartsen in dienst: '
        if len(self.__list_huisartsen) < 1:
            print('geen')
        else:
            for i in self.__list_huisartsen:
                print(i)

