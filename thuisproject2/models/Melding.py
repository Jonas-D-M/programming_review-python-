from models.Locatie import Locatie
from models.logging import melding_properties_logger
from models.logging import melding_static_methods_logger
import json
import string


class Melding():


    __alle_meldingen = []


    def __init__(self, Locatie, categorie, subcategorie, soortbinnenkomst, doorlooptijd : int, meldingsdatum):
        self.locatie = Locatie
        self.categorie = categorie
        self.subcategorie = subcategorie
        self.soortbinnenkomst = soortbinnenkomst
        self.doorlooptijd = doorlooptijd
        self.meldingsdatum = meldingsdatum
        Melding.__alle_meldingen.append(self)


    @property
    def locatie(self):
        return self.__locatie

    @locatie.setter
    def locatie(self, value):
        if isinstance(value, Locatie):
            self.__locatie = value
        else:
            melding_properties_logger.error('Value was not an object of the class locatie')


    @property
    def categorie(self):
        return self.__categorie

    @categorie.setter
    def categorie(self, value):
        if isinstance(value, str):
            self.__categorie = value
        else:
            melding_properties_logger.error('Value for categorie was not a string')


    @property
    def subcategorie(self):
        return self.__subcategorie

    @subcategorie.setter
    def subcategorie(self, value):
        if isinstance(value, str):
            self.__subcategorie = value
        else:
            melding_properties_logger.error('Value for subcategorie was not a string')


    @property
    def soortbinnenkomst(self):
        return self.__soortbinnenkomst

    @soortbinnenkomst.setter
    def soortbinnenkomst(self, value):
        if isinstance(value, str):
            self.__soortbinnenkomst = value
        else:
            melding_properties_logger.error('Value for soortbinnenkomst was not a string')


    @property
    def doorlooptijd(self):
        return self.__doorlooptijd

    @doorlooptijd.setter
    def doorlooptijd(self, value):
        if isinstance(value, int):
            self.__doorlooptijd = value
        else:
            melding_properties_logger.error('Value for doorlooptijd was not an int')


    @property
    def meldingsdatum(self):
        return self.__meldingsdatum

    @meldingsdatum.setter
    def meldingsdatum(self, value):
        if isinstance(value, str):
            self.__meldingsdatum = value
        else:
            melding_properties_logger.error('Value for meldingsdatum was not a string')


    @property
    def info(self):
        return f'Melding: {self}    Datum: {self.meldingsdatum} Categorie: {self.categorie} Sub-Categorie: {self.subcategorie}'


    def __str__(self):
        return f'{self.locatie} categorie: {self.categorie} Sub-categorie: {self.subcategorie}  Soortbinnenkomst: {self.soortbinnenkomst}   Doorlooptijd: {self.doorlooptijd}   Meldingsdatum: {self.meldingsdatum}'


    def __lt__(self, other):
        if self.locatie.straat < other.locatie.straat:
            return True
        else:
            return False


    @staticmethod
    def inlezen_json():
        meldingen = []
        try:
            with open("thuisproject2\\bronbestand\meldingen_2016.json",'r', encoding='utf8') as f:
                data = json.load(f)
                for i in data:
                    lat = i['lat'].replace(",", ".")
                    long = i['lon'].replace(",", ".")
                    locatie = Locatie(i['Straat'], float(lat), float(long))
                    categorie = i['categorie']
                    subcategorie = i['subcategorie']
                    soortbinnenkomst = i['Soortbinnenkomst']
                    doorlooptijd = i['Doorlooptijd']
                    try:
                        doorlooptijd_int = int(doorlooptijd[0:2])
                        meldingsdatum = i['dt_aangemeld']
                        try:
                            melding = Melding(locatie,categorie,subcategorie,soortbinnenkomst,doorlooptijd_int,meldingsdatum)
                            meldingen.append(melding)
                            Melding.__alle_meldingen.append(melding)
                        except ValueError as ve:
                            melding_static_methods_logger.error(ve)
                    except ValueError as ve:
                        melding_static_methods_logger.error(ve)
                melding_static_methods_logger.info(f'File has been read succesfully, {len(meldingen)} objects have been created.')
                f.close()
                return meldingen
        except FileNotFoundError as fn:
            melding_static_methods_logger.error(f'For inlezen_json: {fn}')


    @staticmethod
    def select_categorie(list_meldingen, categorie):
        filtered_list = []
        for i in list_meldingen:
            if isinstance(i, Melding):
                if i.categorie.lower() == categorie.lower():
                    filtered_list.append(i)
            else:
                melding_static_methods_logger.error(f'For select_categorie: Item at index {list_meldingen.index(i)} is not an object of the class Melding.')
        if len(filtered_list) > 0:
            return filtered_list
            melding_static_methods_logger.info(f'Select_method categorie has been executed succesfully, a filtered list of {len(filtered_list)} has been created')
        else:
            melding_static_methods_logger.info('The categorie that was entered does not appear in the list.')


    @staticmethod
    def select_soortbinnenkomst(list_meldingen, soortbinnenkomst):
        filtered_list = []
        for i in list_meldingen:
            if isinstance(i,Melding):
                if i.soortbinnenkomst.lower() == soortbinnenkomst.lower():
                    filtered_list.append(i)
            else:
                melding_static_methods_logger.error(f'For select_soort_binnekomst: Item at index {list_meldingen.index(i)} is not an object of the class Melding.')
        if len(filtered_list) > 0:
            return filtered_list
        else:
            return 'The soortbinnenkomst you have entered does not seem to be in the entered list.'


    @staticmethod
    def analyse_categorien(list_meldingen):
        analyse_dict = {}
        for i in list_meldingen:
            if isinstance(i, Melding):
                if i.categorie not in analyse_dict:
                    analyse_dict.update({i.categorie : 1})
                else:
                    analyse_dict[i.categorie] += 1
            else:
                melding_static_methods_logger.error(f'For analyse_categorie: item at index {list_meldingen.index(i)} is not an object of the class Melding')
        return analyse_dict


    @staticmethod
    def print_meldingen(list_meldingen):
        for i in list_meldingen:
            if isinstance(i, Melding):
                print(i)
            else:
                melding_static_methods_logger.error(f'For print_meldingen: item at index {list_meldingen.index(i)} is not an object of the class Melding')






