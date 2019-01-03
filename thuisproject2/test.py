from models.Melding import Melding
from models.Locatie import Locatie
from models.Stadsmedewerker import Stadsmedewerker

#inlezen van het bronbestand
meldingen = Melding.inlezen_json()

#Lijst meldingen sorteren op basis van adres
sorted(meldingen)

#printen lijst meldingen
Melding.print_meldingen(meldingen)

#Filteren meldingen op basis van categorie
filtered_list_categorie = Melding.select_categorie(meldingen, 'ophaling afval')

#filteren meldingen op basis van soort binnenkomst
filtered_list_soortbinnenkomst = Melding.select_soortbinnenkomst(meldingen, 'e-mail')

#Analyseren van de categorieen
categorie_analyse = Melding.analyse_categorien(meldingen)

#toekennen van een of meerdere meldingen bij een stadsmedewerker
stadsmedewerker1 = Stadsmedewerker('Tom', 'Stevens', 'Groendienst')
locatie1 = Locatie('straat1', 5.0, 6.0)
locatie2 = Locatie('straat2', 3.0, 4.0)
melding1 = Melding(locatie1, 'categorie1','subcat1','email1',25,'datum1')
melding2 = Melding(locatie2, 'categorie2','subcat2','email2',26,'datum2')
stadsmedewerker1.verwerk_nieuwe_melding(melding1, melding2)

#Verwijderen van een afgewerkte melding
stadsmedewerker1.melding_verwerkt(melding1)

#opvragen alle op te volgen meldingen
stadsmedewerker1.geef_alle_meldingen()

