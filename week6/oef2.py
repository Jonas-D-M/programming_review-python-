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

def check_if_file_is_real(file_path):
    try:
        read_file_with_line_numbers(file_path)
    except FileNotFoundError:
        f = open('new_text.txt', 'w+', encoding='utf-8')
        while True:
            line = input('Write a new line for the file, enter q to exit.')
            if line.lower() == 'q':
                f.close()
                break
            else:
                new_line = f.write(f'{line}\n')

check_if_file_is_real('geen file path')