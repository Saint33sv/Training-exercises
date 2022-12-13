from easygui import *
from random import randrange, randint


def rock_paper_scissors():
    n = 'Ничья!'
    w = 'Победа!'
    pr = 'Проигрыш!'
    rock_win = ('rock.png', 'gt.png', 'scissors.png')
    rock_lu = ('rock.png', 'lt.png', 'paper.png')
    rock_eg = ('rock.png', 'eq.png', 'rock.png')
    paper_win = ('paper.png', 'gt.png', 'rock.png')
    paper_lu = ('paper.png', 'lt.png', 'scissors.png')
    paper_eg = ('paper.png', 'eq.png', 'paper.png')
    scissors_win = ('scissors.png', 'gt.png', 'paper.png')
    scissors_lu = ('scissors.png', 'lt.png', 'rock.png')
    scissors_eg = ('scissors.png', 'eq.png', 'scissors.png')
    l_ch = ['Камень', 'Ножницы', 'Бумага']
    ok_ch = ['Ok', 'Yes', 'Go']
    while True:
        comp_ch = l_ch[randrange(len(l_ch))]
        your_ch = buttonbox(msg='Ваш выбор?', title='Камень Ножницы Бумага', image='putin.png', choices=l_ch)
        if your_ch is None:
            break
        if l_ch.index(your_ch) == 0 and comp_ch == l_ch[1]:
            your_ch = buttonbox(msg=f'{w} Ваш выбор?', title='Камень Ножницы Бумага', choices=ok_ch, images=rock_win)
            if your_ch is None:
                break
        elif l_ch.index(your_ch) == 0 and comp_ch == l_ch[2]:
            your_ch = buttonbox(msg=f'{pr} Ваш выбор?', title='Камень Ножницы Бумага', choices=ok_ch, images=rock_lu)
            if your_ch is None:
                break
        elif l_ch.index(your_ch) == 0 and comp_ch == l_ch[0]:
            your_ch = buttonbox(msg=f'{n} Ваш выбор?', title='Камень Ножницы Бумага', choices=ok_ch, images=rock_eg)
            if your_ch is None:
                break
        elif l_ch.index(your_ch) == 1 and comp_ch == l_ch[0]:
            your_ch = buttonbox(msg=f'{pr} Ваш выбор?', title='Камень Ножницы Бумага', choices=ok_ch,
                                images=scissors_lu)
            if your_ch is None:
                break
        elif l_ch.index(your_ch) == 1 and comp_ch == l_ch[2]:
            your_ch = buttonbox(msg=f'{w} Ваш выбор?', title='Камень Ножницы Бумага', choices=ok_ch,
                                images=scissors_win)
            if your_ch is None:
                break
        elif l_ch.index(your_ch) == 1 and comp_ch == l_ch[1]:
            your_ch = buttonbox(msg=f'{n} Ваш выбор?', title='Камень Ножницы Бумага', choices=ok_ch, images=scissors_eg)
            if your_ch is None:
                break
        elif l_ch.index(your_ch) == 2 and comp_ch == l_ch[0]:
            your_ch = buttonbox(msg=f'{w} Ваш выбор?', title='Камень Ножницы Бумага', choices=ok_ch, images=paper_win)
            if your_ch is None:
                break
        elif l_ch.index(your_ch) == 2 and comp_ch == l_ch[1]:
            your_ch = buttonbox(msg=f'{pr} Ваш выбор?', title='Камень Ножницы Бумага', choices=ok_ch, images=paper_lu)
            if your_ch is None:
                break
        elif l_ch.index(your_ch) == 2 and comp_ch == l_ch[2]:
            your_ch = buttonbox(msg=f'{n} Ваш выбор?', title='Камень Ножницы Бумага', choices=ok_ch, images=paper_eg)
            if your_ch is None:
                break


def guess_the_number():
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


games = [
    'Камень, ножницы, бумага',
    'Угадай число'
]

games_entry_points = [
    rock_paper_scissors,
    guess_the_number
]

while True:
    res = buttonbox('Выбери игру!', choices=games)
    if res is None:
        break
    games_entry_points[games.index(res)]()

