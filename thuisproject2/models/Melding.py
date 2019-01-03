from models.Locatie import Locatie
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
            raise ValueError('Can only be an object of the class locatie')


    @property
    def categorie(self):
        return self.__categorie

    @categorie.setter
    def categorie(self, value):
        if isinstance(value, str):
            self.__categorie = value
        else:
            raise ValueError('categorie needs to be a string')


    @property
    def subcategorie(self):
        return self.__subcategorie

    @subcategorie.setter
    def subcategorie(self, value):
        if isinstance(value, str):
            self.__subcategorie = value
        else:
            raise ValueError('subcategorie needs to be a string')


    @property
    def soortbinnenkomst(self):
        return self.__soortbinnenkomst

    @soortbinnenkomst.setter
    def soortbinnenkomst(self, value):
        if isinstance(value, str):
            self.__soortbinnenkomst = value
        else:
            raise ValueError('soortbinnenkomst needs to be a string')


    @property
    def doorlooptijd(self):
        return self.__doorlooptijd

    @doorlooptijd.setter
    def doorlooptijd(self, value):
        if isinstance(value, int):
            self.__doorlooptijd = value
        else:
            raise ValueError('doorlooptijd needs to be an int.')


    @property
    def meldingsdatum(self):
        return self.__meldingsdatum

    @meldingsdatum.setter
    def meldingsdatum(self, value):
        if isinstance(value, str):
            self.__meldingsdatum = value
        else:
            raise ValueError('meldingsdatum needs to be a string, format (dd/mm/yyyy)')


    @property
    def info(self):
        return f'Melding: {self}    Datum: {self.meldingsdatum} Categorie: {self.categorie} Sub-Categorie: {self.subcategorie}'


    def __str__(self):
        return f'{self.locatie} categorie: {self.categorie} Sub-categorie: {self.subcategorie}  Soortbinnenkomst: {self.soortbinnenkomst}   Doorlooptijd: {self.doorlooptijd}   Meldingsdatum: {self.meldingsdatum}'


    def __lt__(self, other):
        if self.categorie < other.categorie:
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
                    doorlooptijd_int = int(doorlooptijd[0:2])
                    meldingsdatum = i['dt_aangemeld']
                    melding = Melding(locatie,categorie,subcategorie,soortbinnenkomst,doorlooptijd_int,meldingsdatum)
                    meldingen.append(melding)
                    Melding.__alle_meldingen.append(melding)
                f.close()
                return meldingen
        except FileNotFoundError:
            print('The file path you have entered does not seem to exist.')


    @staticmethod
    def select_categorie(list_meldingen, categorie):
        filtered_list = []
        for i in list_meldingen:
            if isinstance(i, Melding):
                if i.categorie.lower() == categorie.lower():
                    filtered_list.append(i)
            else:
                raise ValueError(f'Item at index {list_meldingen.index(i)} is not an object of the class Melding.')
        if len(filtered_list) > 0:
            return filtered_list
        else:
            return 'The categorie you have entered does not appear in the list.'


    @staticmethod
    def select_soortbinnenkomst(list_meldingen, soortbinnenkomst):
        filtered_list = []
        for i in list_meldingen:
            if isinstance(i,Melding):
                if i.soortbinnenkomst.lower() == soortbinnenkomst.lower():
                    filtered_list.append(i)
            else:
                raise ValueError(f'Item at index {list_meldingen.index(i)} is not an object of the class Melding.')
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
                raise ValueError(f'item at index {list_meldingen.index(i)} is not an object of the class Melding')
        return analyse_dict






