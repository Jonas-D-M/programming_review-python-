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
        self.__straat = value


    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        if isinstace(value, float):
            self.__latitude = value
        else:
            raise ValueError('De instantie latitude mag enkel een float zijn.')


    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        if isinstance(value, float):
            self.__longitude = value
        else:
            raise ValueError('De instantie longitude mag enkel een float zijn.')



