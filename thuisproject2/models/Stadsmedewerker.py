


class Stadsmedewerker():


    def __init__(self, voornaam, naam, dienst):
        self.voornaam = voornaam
        self.naam = naam
        self.dienst = dienst
        self.__te_verwerken = []


    @property
    def voornaam(self):
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value):
        if isinstance(value, str):
            self.__voornaam = value
        else:
            raise ValueError('voornaam needs to be a string.')


    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        if isinstance(value, str):
            self.__naam = value
        else:
            raise ValueError('naam needs to be a string')


    @property
    def dienst(self):
        return self.__dienst

    @dienst.setter
    def dienst(self, value):
        if isinstance(value, str):
            self.__dienst = value
        else:
            raise ValueError('dienst needs to be a string.')


    @property
    def te_verwerken(self):
        return self.__te_verwerken

    @te_verwerken.setter
    def te_verwerken(self, value):
        if isinstance (value, Melding):
            self.__te_verwerken.append(value)
        else:
            raise ValueError('Only object of the class Melding can be added to the list of te verwerken meldingen.')
