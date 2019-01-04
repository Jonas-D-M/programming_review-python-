import logging
from models.logger import  bier_properties_logger
from models.logger import bier_file_reader_logger
from models.logger import bier_opnaam_logger
from models.logger import bier_opalcohol_logger
from models.logger import bier_opbrouwerij_logger


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
        self.__brouwerijnaam = value



    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        self.__kleur = value



    @property
    def alcoholpercentage(self):
        return self.__alcoholpercentage

    @alcoholpercentage.setter
    def alcoholpercentage(self, value):
        if isinstance(value, float):
            self.__alcoholpercentage = value
        else:
            bier_properties_logger.error('The variable entered for alcoholpercentage was not a float.')



    def __str__(self):
        return f'biernaam: {self.biernaam}  brouwerijnaam: {self.brouwerijnaam} kleur: {self.kleur} alcoholpercentage: {self.alcoholpercentage}'


    def __lt__(self, other):
        if self.alcoholpercentage < other.alcoholpercentage:
            return True
        else:
            return False


    @staticmethod
    def try_convert(value):
        try:
            float(value)
            return True
        except ValueError:
            return False


    @staticmethod
    def inlezen_bieren():
        list_bieren = []
        try:
            counter_goed = 0
            counter_slecht = 0
            with open('week11\\bronbestand\\bieren.txt') as f:
                for line in f:
                    bier_file_reader_logger.info(f'Lijn: {line} werd ingelezen')
                    line = line.strip().split(';')
                    biernaam = line[1]
                    brouwerijnaam = line[2]
                    kleur = line[3]
                    alcoholpercentage = line[4]
                    if Bier.try_convert(alcoholpercentage):
                        try:
                            bier = Bier(biernaam, brouwerijnaam, kleur, float(alcoholpercentage))
                            list_bieren.append(bier)
                            counter_goed += 1
                            bier_file_reader_logger.info(f'Object: {bier} werd aangemaakt')
                        except:
                            bier_file_reader_logger.error('Deze lijn was niet correct geformateerd.')
                    else:
                        bier_file_reader_logger.error('Deze lijn was niet correct geformateerd.')
                        counter_slecht += 1
                bier_file_reader_logger.info(f'Het aantal object dat werd aangemaakt is: {counter_goed}')
                bier_file_reader_logger.info(f'Het aantal lijnen dat niet kon worden ingelezen is: {counter_slecht}.')
                f.close()
            return list_bieren
        except FileNotFoundError:
            bier_file_reader_logger.error('De file path is niet correct.')


    @staticmethod
    def zoek_bieren_op_naam(list_bieren, naam):
        filtered_list = []
        for i in list_bieren:
            if isinstance (i, Bier):
                if naam.lower() in i.biernaam.lower() :
                    filtered_list.append(i)
                    bier_opnaam_logger.info(f'Object {i} has been added to the filtered list')
            else:
                bier_opnaam_logger.error(f'object at index {list_bieren.index(i)} was not an object of the class Bier')
        return filtered_list


    @staticmethod
    def zoek_bieren_op_alcoholpercentage(list_bieren, min_percentage, max_percentage):
        filtered_list = []
        for i in list_bieren:
            if isinstance(i, Bier):
                if i.alcoholpercentage > min_percentage and i.alcoholpercentage < max_percentage:
                    filtered_list.append(i)
                    bier_opalcohol_logger.info(f'object: {i} has been added to the filtered list.')
            else:
                bier_opalcohol_logger.error(f'object at index {list_bieren.index(i)} was not an object of the class Bier')
        return filtered_list



    @staticmethod
    def zoek_bieren_op_brouwerij(list_bieren, brouwerij):
        filtered_list = []
        for i in list_bieren:
            if isinstance(i, Bier):
                if i.brouwerijnaam.lower() == brouwerij:
                    filtered_list.append(i)
                    bier_opbrouwerij_logger.info(f'Object: {i} has been added to the filtered list.')
            else:
                bier_opbrouwerij_logger.error(f'object at index {list_bieren.index(i)} was not an object of the class bier')
        return filtered_list