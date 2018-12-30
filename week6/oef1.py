def read_file_with_line_numbers(file_path):
    with open(file_path, 'r', encoding='utf-8') as fo:
        line = fo.readline()
        counter = 1
        while line:
            line.strip('\n')
            print(f'{counter}. {line}')
            line = fo.readline()
            counter += 1
        fo.close()

read_file_with_line_numbers('week6/tekst.txt')