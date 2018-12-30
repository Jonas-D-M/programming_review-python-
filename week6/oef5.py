import re

def inlezen_bestand(file_path):
    students_score = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as fo:
            line = fo.readline()
            while line:
                line = re.sub(r':', ' ', line).strip('\n').split()
                name_sequence = (line[0], line[1])
                score = line[2:]
                students_score.update({' '.join(name_sequence) : score})
                line = fo.readline()
            fo.close()
        return students_score
    except FileNotFoundError:
        print('the file path you have entered does not exist.')


students = inlezen_bestand('bronbestanden\Scores.txt')

for k,v in students.items():
    print(f'Student: {k} geeft de volgende scores behaald:\n{v}')
