def file_write_lines():
    new_file = open(r'C:\Users\Lam\Desktop\data.txt', 'w')
    while True:
        info_user = input('Введите строку для записи: ')
        if len(info_user) > 0:
            new_file.write(f'{info_user}\n')
        else:
            break

    new_file.close()
    print('Файл записан!')


def show_file():
    info_user = input('Укажите путь и имя файла: ')
    open_file = open(info_user, 'r')
    print(open_file.read())
    open_file.close()


def show_file_lines():
    info_user = input('Укажите путь и имя файла: ')
    open_file = open(info_user, 'r')
    read_file = open_file.readlines()
    for i in range(len(read_file)):
        print(f'{i+1} {read_file[i]}')
    open_file.close()


show_file_lines()
