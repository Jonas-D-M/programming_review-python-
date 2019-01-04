import logging
from models.logger import  bier_properties_logger
from models.logger import bier_file_reader_logger


class Bier():


    def __init__(self, biernaam, brouwerijnaam, kleur, alcoholpercentage : float):
        self.biernaam = biernaam
        self.brouwerijnaam = brouwerijnaam
        self.kleur = kleur
        self.alcoholpercentage = alcoholpercentage


    @property
    def biernaam(self):
        return self.__biernaam

    @biernaam.setter
    def biernaam(self, value):
        if isinstance(value, str) and value != '':
            self.__biernaam = value
        else:
            bier_properties_logger.error('The variable entered for biernaam was not a string or empty')



    @property
    def brouwerijnaam(self):
        return self.__brouwerijnaam

    @brouwerijnaam.setter
    def brouwerijnaam(self, value):
        if isinstance(value, str) and value != '':
            self.__brouwerijnaam = value
        else:
            bier_properties_logger.error('The variable entered for brouwerijnaam was not a string or empty')


    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        if isinstance(value, str) and value != '':
            self.__kleur = value
        else:
            bier_properties_logger.error('The variable entered for kleur was not a string or empty')


    @property
    def alcoholpercentage(self):
        return self.__alcoholpercentage

    @alcoholpercentage.setter
    def alcoholpercentage(self, value):
        if isinstance(value, float):
            self.__alcoholpercentage = value
        else:
            bier_properties_logger.error('The variable entered for alcoholpercentage was not a float.')



