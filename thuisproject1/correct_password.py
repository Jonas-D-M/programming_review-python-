import re
import random as rd
import string


def password_control(apassword):
    if not re.search(r'[a-z]',apassword):
        return False
    elif not re.search(r'[0-9]', apassword):
        return False
    elif not re.search(r'[A-z]', apassword):
        return False
    elif not re.search(r'[$,@,#]', apassword):
        return False
    elif not len(apassword) > 9  and len(apassword) < 19:
        return False
    else:
        return True


def generate_correct_password():
    password = ''
    password += rd.choice(string.ascii_lowercase)*5
    password += rd.choice(string.ascii_uppercase)*3
    password += str(rd.randrange(0,9)) * 3
    sequence = ('@', '#', '$')
    password += rd.choice(sequence)
    return password


correct_password = generate_correct_password()
print(correct_password)
print(password_control(correct_password))
print(password_control('a'))