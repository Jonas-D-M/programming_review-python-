from models.Handelszaak import Handelszaak
from models.logger import huisartspraktijk_properties_logger
from models.logger import huisartspraktijk_methods_logger
import csv


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
        return f'{super().__str__()}  praktijktype: {self.praktijktype}'


    def voeg_huisarts_toe(self,huisarts):
        self.__list_huisartsen.append(huisarts)
        huisartspraktijk_methods_logger.info(f'huisarts {huisarts} werd toegevoegd aan {self}.')


    @staticmethod
    def inlezen_huisartsen(file_path):
        praktijken = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.replace('"', '')
                    line = line.strip().split(';')
                    arts = line[1]
                    huisnummer = line[2]
                    praktijktype = line[3]
                    straat = line[4]
                    gemeente = line[5]
                    postcode = line[6]
                    telefoonnummer = line[7]
                    try:
                        praktijk = Huisartspraktijk(straat, int(huisnummer), int(postcode), gemeente, telefoonnummer, praktijktype)
                        if praktijk not in praktijken:
                            praktijken.append(praktijk)
                            praktijk.voeg_huisarts_toe(arts)
                        else:
                            praktijk.voeg_huisarts_toe(arts)
                    except ValueError as ve:
                        huisartspraktijk_methods_logger.error(f'For inlezen huisartsen: {ve}')
            f.close()
            huisartspraktijk_methods_logger.info(f'For inlezen huisartsen: Het bestand werd succesvol ingelezen, het aantal toegevoegde praktijken is {len(praktijken)}')
            return praktijken
        except FileNotFoundError as fe:
            huisartspraktijk_methods_logger.error(f'for inlezen huisartsen: {fe}')


    @staticmethod
    def zoek_info_arts(praktijken, arts):
        filtered_list = []
        if isinstance(praktijken, list) and isinstance(arts, str):
            for i in praktijken:
                if isinstance(i, Huisartspraktijk):
                    for k in i.__list_huisartsen:
                        if arts.lower() in k.lower():
                            filtered_list.append(i)
                            huisartspraktijk_methods_logger.info(f'For zoek info arts: De volgend praktijk werd toegevoegd aan de lijst: {i}')
                else:
                    huisartspraktijk_methods_logger.error(f'for zoek info arts: the object at index {praktijken.index(i)} does not belong to the class Huisartspraktijk.')
        else:
            huisartspraktijk_methods_logger.error('for zoek info arts: input needs te be a list, arts needs to be a string')
        if len(filtered_list) != 0:
            for i in filtered_list:
                print(i)
                for k in i.__list_huisartsen:
                    print(k)


    @staticmethod
    def print_info_alle_praktijken(praktijken):
        if isinstance(praktijken, list):
            for i in praktijken:
                if isinstance(i, Huisartspraktijk):
                    print(f'{i} \n gevestigde huisartsen:')
                    for k in i.__list_huisartsen:
                        print(k)
                else:
                    huisartspraktijk_methods_logger.error(f'for print alle praktijken: the object at index {praktijken.index(i)} was not of the class Huisartspraktijk')
        else:
            huisartspraktijk_methods_logger.error('for print alle praktijken: input needs to be a list.')





