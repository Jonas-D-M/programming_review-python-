from models.Melding import Melding
from models.Locatie import Locatie


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


    def __str__(self):
        return f'Voornaam: {self.voornaam}  Naam: {self.naam}   Dienst: {self.dienst} heeft de volgende meldingen te verwerken: '
        for i in self.__te_verwerken:
            print(i)


    def __lt__(self, other):
        if self.naam.lower() < other.naam.lower():
            return True
        else:
            return False


    def __eq__(self, other):
        if self.naam.lower() == other.naam.lower() and self.voornaam.lower() == other.voornaam.lower() and self.dienst.lower() == other.dienst.lower():
            return True
        else:
            return False


    def verwerk_nieuwe_meldingen(self, *args):
        for i in args:
            self.__te_verwerken.append(i)


    def selecteer_mijn_melding(self,  meldingen, categorie):
        filtered_list = []
        for i in meldingen:
            if isinstance(i, Melding):
                if i.categorie.lower() == categorie.lower():
                    filtered_list.append(i)
            else:
                raise ValueError(f'Item at index {meldingen.index(i)} is not an object of the class Melding')
        return filtered_list


    def melding_verwerkt(self, melding):
        if isinstance(melding, Melding):
            if melding in self.__te_verwerken:
                self.__te_verwerken.remove(melding)
            else:
                raise ValueError('The melding you have entered does not appear in the te_verwerken list.')
        else:
            raise ValueError('Needs to be an object of the class Melding')