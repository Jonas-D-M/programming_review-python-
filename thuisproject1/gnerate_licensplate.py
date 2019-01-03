import random as rd
import string

""" This method will generate a random license plate consisting of one number, 3 uppercase letters and 3 random numbers
all separated by a - """
def generate_licenseplate ():
    licenseplate = ''
    licenseplate += str(rd.randrange(0,9))
    licenseplate += '-'
    for i in range(0,3):
        licenseplate += rd.choice(string.ascii_uppercase)
    licenseplate += '-'
    for i in range(0,3):
        licenseplate += str(rd.randrange(0,9))
    return licenseplate


""" Method to print x plates, x being the desired number of plates entered as a parameter """
def amount_of_plates (x):
    plates = []
    for i in range( 0, x):
        plates.append(generate_licenseplate())

    for i in plates:
        print (i)

try:
    amount = int(input('Enter the amount of licenseplates you wish to generate, needs to be an int'))
except ValueError:
    print('your input was not an int')

amount_of_plates(amount)
