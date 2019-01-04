from models.logger import adres_properties_logger


class Adres():


    def __init__(self, straat, huisnummer : int, postcode : int, gemeente):
        self.straat = straat
        self.huisnummer = huisnummer
        self.postcode = postcode
        self.gemeente = gemeente


    @property
    def straat(self):
        return self.__straat

    @straat.setter
    def straat(self, value):
        if isinstance(value, str):
            self.__straat = value
        else:
            adres_properties_logger.error('Straat has to be a string.')


    @property
    def huisnummer(self):
        return self.__huisnummer

    @huisnummer.setter
    def huisnummer(self, value):
        if isinstance(value, int):
            self.__huisnummer = value
        else:
            adres_properties_logger.error('huisnummer needs to be an int.')


    @property
    def postcode(self):
        return self.__postcode

    @postcode.setter
    def postcode(self, value):
        if isinstance(value, int):
            self.__postcode = value
        else:
            adres_properties_logger.error('postcode needs to be an int.')


    @property
    def gemeente(self):
        return self.__gemeente

    @gemeente.setter
    def gemeente(self, value):
        if isinstance(gemeente, str):
            self.__gemeente = value
        else:
            adres_properties_logger.error('Gemeente needs to be a string')
