import random as rd

def inlezen_spelers(file_path):
    list_spelers = []
    try:
        with open(file_path, 'r', encoding='utf-8') as fo:
            for line in fo:
                list_spelers.append(line)
            fo.close()
    except FileNotFoundError:
        print('The file path you have entered does not exist.')
    return list_spelers

file_list_spelers = inlezen_spelers('bronbestanden\Spelers.txt')


def afprinten_spelers(list_spelers):
    for i in list_spelers:
        print(i)

def selecteer_random_elftal(list_spelers):
    with open('bronbestanden\random_elftal.txt', 'w+', encoding='utf-8') as fo:
        i = 0
        while i < 11:
            speler = list_spelers[rd.randrange(0,len(list_spelers))]
            if speler not in fo:
                fo.write(f'{speler}\n')
                i += 1
        fo.close()

selecteer_random_elftal(file_list_spelers)
