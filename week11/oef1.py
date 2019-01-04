import logging
import random

logging.basicConfig(filename='logs.txt', level=logging.DEBUG)

def genereer_even_getallen(aantal):
    even_getallen = []

    while len(even_getallen) != aantal:
        getal = random.randint(0, 1000)
        logging.info('Gekozen getal: %d' % (getal))
        if getal % 2 == 0 and (not getal in even_getallen):
            even_getallen.append(getal)
    logging.info("De lijst met even getallen: %s" % even_getallen)
    return even_getallen

aantal = int(input("Geef een aantal getallen op:> "))
resultaat = genereer_even_getallen(aantal)
logging.info("De gekozen even getallen zijn: %s " % resultaat)