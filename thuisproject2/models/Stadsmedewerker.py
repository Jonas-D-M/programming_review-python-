from models.Melding import Melding
from models.Locatie import Locatie
from logging import stadsmedewerker_properties_logger
from logging import stadsmedewerker_methods_logger


class Stadsmedewerker():


    def __init__(self, voornaam, naam, dienst):
        self.voornaam = voornaam
        self.naam = naam
        self.dienst = dienst
        self.__meldingen = []


    @property
    def voornaam(self):
        return self.__voornaam

    @voornaam.setter
    def voornaam(self, value):
        if isinstance(value, str):
            self.__voornaam = value
        else:
            stadsmedewerker_properties_logger.error('voornaam needs to be a string.')


    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        if isinstance(value, str):
            self.__naam = value
        else:
            stadsmedewerker_properties_logger.error('naam needs to be a string')


    @property
    def dienst(self):
        return self.__dienst

    @dienst.setter
    def dienst(self, value):
        if isinstance(value, str):
            self.__dienst = value
        else:
            stadsmedewerker_properties_logger.error('dienst needs to be a string.')


    @property
    def meldingen(self):
        return self.__meldingen

    @meldingen.setter
    def meldingen(self, value):
        if isinstance (value, Melding):
            self.__meldingen.append(value)
        else:
            stadsmedewerker_properties_logger.error('Only object of the class Melding can be added to the list of te verwerken meldingen.')


    def __str__(self):
        return f'Voornaam: {self.voornaam}  Naam: {self.naam}   Dienst: {self.dienst} heeft de volgende meldingen te verwerken: '
        for i in self.__meldingen:
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


    def verwerk_nieuwe_melding(self, *args):
        for i in args:
            if isinstance(i, Melding):
                self.__meldingen.append(i)
            else:
                stadsmedewerker_methods_logger.error(f'For verwerk nieuwe melding: item at index {args.index(i)} was not an object of the class meldig.')


    def selecteer_mijn_meldingen(self,  meldingen, categorie):
        filtered_list = []
        for i in meldingen:
            if isinstance(i, Melding):
                if i.categorie.lower() == categorie.lower():
                    filtered_list.append(i)
            else:
                stadsmedewerker_methods_logger.error(f'For selecteer_mijn_melding: Item at index {meldingen.index(i)} is not an object of the class Melding')
        return filtered_list


    def melding_verwerkt(self, melding):
        if isinstance(melding, Melding):
            if melding in self.__meldingen:
                self.__meldingen.remove(melding)
            else:
                stadsmedewerker_methods_logger.error('For melding verwerkt: The melding you have entered does not appear in the te_verwerken list.')
        else:
            stadsmedewerker_methods_logger.error('For melding verwerkt: Needs to be an object of the class Melding')


    def geef_alle_meldingen(self):
        for i in self.__meldingen:
            print(i)