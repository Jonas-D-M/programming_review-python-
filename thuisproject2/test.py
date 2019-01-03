from models.Melding import Melding
from models.Locatie import Locatie
from models.Stadsmedewerker import Stadsmedewerker


meldingen = Melding.inlezen_json("thuisproject2\\bronbestand\meldingen_2016.json")


filtered_list = Melding.select_categorie(meldingen, 'sluikstort')

filtered_dict = Melding.analyse_categorie(meldingen)

for k,v in filtered_dict.items():
    print(k,v)

