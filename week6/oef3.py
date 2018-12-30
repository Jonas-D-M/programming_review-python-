def vul_bestand_aan(file_path):
    try:
        with open(file_path, 'a+', encoding='utf-8') as fo:
            while True:
                new_line = input('Write a line you wish to add to this file. Enter q to exit')
                if new_line == 'q':
                    fo.close()
                    break
                else:
                    fo.write(f'{new_line}\n')
    except FileNotFoundError:
        print('The file path you have entered does not exist, a new file has been created. You can now add new lines to it.')
        with open('new_file.txt', 'w+', encoding='utf-8') as fo:
            while True:
                new_line = input('Enter a new line you wish to add to your file, enter q to exit')
                if new_line == 'q':
                    fo.closed()
                    break
                else:
                    fo.write(f'{new_line}\n')

vul_bestand_aan('week6/tekst.txt')
