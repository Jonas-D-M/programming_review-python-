from models.Locatie import Locatie


class Melding():


    def __init__(self, Locatie, categorie, subcategorie, soortbinnenkomst, doorlooptijd : int, meldingsdatum):
        self.locatie = Locatie
        self.categorie = categorie
        self.subcategorie = subcategorie
        self.soortbinnenkomst = soortbinnenkomst
        self.doorlooptijd = doorlooptijd
        self.meldingsdatum = meldingsdatum


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




