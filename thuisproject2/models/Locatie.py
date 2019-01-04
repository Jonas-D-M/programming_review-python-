from models.logging import locatie_logger



class Locatie:

    def __init__(self, straat, latitude : float, longitude : float):
        self.straat = straat
        self.latitude = latitude
        self.longitude = longitude


    @property
    def straat(self):
        return self.__straat

    @straat.setter
    def straat(self, value):
        if isinstance(value, str):
            self.__straat = value
        else:
            locatie_logger.error('De value voor straat was geen string.')


    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if isinstance(value, float):
            self.__latitude = value
        else:
            locatie_logger.error('De value voor latitude was geen float.')


    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if isinstance(value, float):
            self.__longitude = value
        else:
            locatie_logger.error('De value voor longitude was geen float.')


    def __str__(self):
        return f'Straat: {self.straat}  Latitude: {self.latitude}   Longitude: {self.longitude}'


    def __lt___(self, other):
        if self.straat.lower() < other.straat.lower():
            return True
        else:
            return False


    def __eq__ (self, other):
        if self.straat.lower() == other.straat.lower() and self.latitude == other.latitude and self.longitude == other.longitude:
            return True
        else:
            return False



