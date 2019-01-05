from models.Adres import Adres
from models.Handelszaak import Handelszaak
from models.Huisartspraktijk import Huisartspraktijk


# straat, huisnummer, postcode, gemeente, telefoonnummer, praktijktype/
huisartspraktijk = Huisartspraktijk('straat', 18, 8500,'gemeente','telefoonnummer', 'praktijktype')
print(huisartspraktijk)

with open('oefen_examen\\bronbestand\huisartsen.csv', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.replace('"', '')
        line = line.strip().split(';')
        print(line)
    f.close()