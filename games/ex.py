from easygui import *
from random import randint
comp_num = randint(1, 100)
num_try = 0
while num_try < 10:
    yor_ch = integerbox(msg='Угадай число от 1 до 100', title='Игра', lowerbound=1, upperbound=100)
    if yor_ch is None:
        break
    if yor_ch > comp_num:
        msgbox(msg='Ваше число больше', title='Игра', image='gt.png')
        num_try += 1
        if yor_ch is None:
            break
    elif yor_ch < comp_num:
        msgbox(msg='Ваше число меньше', title='Игра', image='lt.png')
        num_try += 1
        if yor_ch is None:
            break
    elif yor_ch == comp_num:
        msgbox(msg='Вы победили!', title='Победа!!!', image='timon.png')
        if yor_ch is None:
            break
    else:
        msgbox(msg='Не корректное число!', title='Ошибка!!!', image='jab.png')
        break
