from models.Adres import Adres
from models.Handelszaak import Handelszaak
from models.Huisartspraktijk import Huisartspraktijk


# straat, huisnummer, postcode, gemeente, telefoonnummer, praktijktype/
huisartspraktijk = Huisartspraktijk('straat', 18, 8500,'gemeente','telefoonnummer', 'praktijktype')
print(huisartspraktijk)