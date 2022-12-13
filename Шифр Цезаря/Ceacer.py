from alfavit import *
from easygui import *

sym1 = fileopenbox(msg=None, title=None)
sym2 = filesavebox(msg=None, title=None)
num = integerbox(msg='Укажите ключ к шифрованию', title='Шифрование сайта.')


def encode_symbol(symbol, key):
    mesto = alfavit_EU.find(symbol.upper())
    new_mesto = mesto + key
    new_symbol = alfavit_EU[new_mesto]
    return new_symbol


def encode_str(str_, key):
    new_str = ''
    for i in str_:
        mesto = alfavit_EU.find(i.upper())
        new_mesto = mesto + key
        if i.upper() in alfavit_EU:
            new_str += alfavit_EU[new_mesto]
        else:
            new_str += i
    return new_str


def encode_file(input_file_path, output_file_path, key):
    file = open(input_file_path, 'r')
    new_file = open(output_file_path, 'w')
    for i in file.read():
        mesto = alfavit_EU.find(i.upper())
        new_mesto = mesto + key
        if i.upper() in alfavit_EU:
            new_file.write(alfavit_EU[new_mesto])
        else:
            new_file.write(i)
    file.close()
    new_file.close()


encode_file(sym1, sym2, num)



