from models.Locatie import Locatie
from models.Melding import Melding
from models.Stadsmedewerker import Stadsmedewerker


def print_meldingen(list_meldingen):
    # list_meldingen.sort()
    for meld in list_meldingen:
        print(meld.info)


# testen van de individuele klasses
# locatie = Locatie("Graaf Karel de Goedelaan", 50.8444585318144, 3.2347287708217)
# print(locatie)

# melding = Melding(locatie, "Verkiezingen", "Te lange wachtrijen", "e-mail", 20,"5-12-2018")
# print(melding)
# print(melding.info)

# test_medewerker = Stadsmedewerker("Desprinter", "Jacques", "Bevolking")
# print(test_medewerker)

# test_medewerker.verwerk_nieuwe_melding(melding)
# print("\nDe toegekende meldingen van %s (dienst %s) zijn:" % (test_medewerker, test_medewerker.dienst))
# print_meldingen(test_medewerker.meldingen)
# test_medewerker.melding_verwerkt(melding)

# voorbeeld output:
# DESPRINTER, Jacques
# GRAAF KAREL DE GOEDELAAN
# Melding op 5-12-2018 in GRAAF KAREL DE GOEDELAAN
# Melding op 5-12-2018 in GRAAF KAREL DE GOEDELAAN -> Verkiezingen (Te lange wachtrijen)
#
# De toegekende meldingen van DESPRINTER, Jacques (dienst Bevolking) zijn:
# Melding op 5-12-2018 in GRAAF KAREL DE GOEDELAAN -> Verkiezingen (Te lange wachtrijen)


# testen van inlezen file

# inlezen json-file
meldingen = Melding.inlezen_json()
# print("\nAlle ingelezen en verwerkte meldingen zijn:")
# print_meldingen(meldingen)
# # Voorbeeld output:
# # Melding op 05-11-2018 in KWABRUGSTRAAT -> gemeenteweg (put/verzakking)
# # Melding op 05-11-2018 in NOORDSTRAAT -> sluikstort (sluikstort opruimen)
# # Melding op 05-11-2018 in SCHEPENHUISSTRAAT -> park-, groenonderhoud (bladval)
# # ...


# # selectie van meldingen die te maken hebben met overlast
# selectie = Melding.select_categorie(meldingen, "overlast")
# print("\nDit zijn meldingen die gaan over overlast:")
# print_meldingen(selectie)
# # Voorbeeld output:
# # Melding op 05-11-2018 in KRUISBOOMSTRAAT -> overlast (overlast algemeen)
# # Melding op 05-11-2018 in DAM -> overlast (fietsen achtergelaten/wrakken)
# # Melding op 06-11-2018 in DOORNIKSESTEENWEG -> overlast (fietsen achtergelaten/wrakken)
# # Melding op 06-11-2018 in KONSTANT PERMEKELAAN -> overlast (fietsen achtergelaten/wrakken)
# # ...


# # selectie van meldingen die per e-mail binnengekozen zijn
# selectie = Melding.select_soortbinnenkomst(meldingen, "e-mail")
# print("\nDit zijn meldingen die per e-mail binnenkwamen:")
# print_meldingen(selectie)
# # Voorbeeld output:
# # Melding op 05-11-2018 in SCHEPENHUISSTRAAT -> park-, groenonderhoud (bladval)
# # Melding op 05-11-2018 in KONING ALBERTPARK -> sluikstort (sluikstort opruimen)
# # Melding op 05-11-2018 in TORKONJESTRAAT -> signalisatie (straatnaambord)
# # Melding op 05-11-2018 in BISSEGEMSESTRAAT -> signalisatie (verkeersborden)
# # ...


# print("\nDit is de analyse van de categorieën van de meldingen:")
# dict_analyse = Melding.analyse_categorien(meldingen)
# for key, value in dict_analyse.items():
#     print("%s: %d" % (key, value))
# # Voorbeeld output:
# # gemeenteweg: 18
# # sluikstort: 33
# # park-, groenonderhoud: 80
# # signalisatie: 33
# # dieren: 26
# # straatmeubilair: 43
# # ophaling afval: 91
# # ...


medewerker1 = Stadsmedewerker("Walcarius", "Stijn", "Groendienst")
medewerker2 = Stadsmedewerker("Roobrouck", "Dieter", "Verkeer")
medewerker3 = Stadsmedewerker("Vannieuwenhuyse", "Johan", "IMOG")  #afval
medewerker4 = Stadsmedewerker("Laprudence", "Christophe", "VLAS") #politie

medewerker1.selecteer_mijn_meldingen(meldingen, "groen")
print("\nDe meldingen voor %s (dienst %s) zijn:" % (medewerker1, medewerker1.dienst))
print_meldingen(medewerker1.meldingen)
# # Voorbeeld output:
# # De meldingen voor WALCARIUS, Stijn (dienst Groendienst) zijn:
# # Melding op 05-11-2018 in SCHEPENHUISSTRAAT -> park-, groenonderhoud (bladval)
# # Melding op 05-11-2018 in MARKSESTEENWEG -> park-, groenonderhoud (vraag voor onderhoud)
# # Melding op 05-11-2018 in VOORUITGANGSSTRAAT -> park-, groenonderhoud (onkruid niet verwijderd)
# # Melding op 05-11-2018 in EMIEL HULLEBROECKLAAN -> park-, groenonderhoud (bladval)
# # ...


# # ANALOOG
# # medewerker2.selecteer_mijn_meldingen(meldingen,"groen")
# # print("\nDe meldingen voor %s zijn:" % medewerker2)
# # print_meldingen(medewerker2.meldingen)
# #
# # medewerker3.selecteer_mijn_meldingen(meldingen,"afval")
# # print("\nDe meldingen voor %s zijn:" % medewerker3)
# # print_meldingen(medewerker3.meldingen)
# #
# # medewerker4.selecteer_mijn_meldingen(meldingen,"overlast")
# # print("\nDe meldingen voor %s zijn:" % medewerker4)
# # print_meldingen(medewerker4.meldingen)
