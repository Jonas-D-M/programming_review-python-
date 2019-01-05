from models.logger import hotelkamer_properties_logger
from models.Hotelgast import Hotelgast


class Hotelkamer():


    def __init__(self, kamernummer : int):
        self.kamernummer = kamernummer
        self.__gastenlijst = []


    @property
    def kamernummer(self):
        return self.__kamernummer

    @kamernummer.setter
    def kamernummer(self, value):
        if isinstance(value, int):
            self.__kamernummer = value
        else:
            hotelkamer_properties_logger.error('kamernummer needs to be an int')


    @property
    def gastenlijst(self):
        return self.__gastenlijst

    @gastenlijst.setter
    def gastenlijst(self, value):
        if isinstance(value, Hotelgast):
            self.__gastenlijst = value
        else:
            hotelkamer_properties_logger.error('Only objects of the class hotelgast kan be added to the gastenlijst')

