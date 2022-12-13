from easygui import *


def first_liters(player):
    return player[0]


def last_liters(player):
    return (player[-1])


choise1 = str()
choise2 = str()
start_game = True
while True:
    player_1 = enterbox('Игрок 1. Введите слово', 'Игра "Города"!')
    if player_1 is None:
        break
    choise1 = player_1
    if start_game or last_liters(choise2.lower()) == first_liters(player_1.lower()):
        if msgbox(f'Ваше слово должно начинаться с буквы: "{last_liters(player_1).upper()}"', 'Игра "Города"!')\
                is None:
            break
    elif last_liters(choise2.lower()) != first_liters(player_1.lower()):
        if msgbox(f'Игрок1 НЕВЕРНО!!!Ваше слово должно начинаться с буквы: "{last_liters(choise2).upper()}"',
                  'Игра "Города"!') is None:
            break
        continue
    start_game = False
    true_or_falce = 0
    while true_or_falce <= 0:
        player_2 = enterbox('Игрок 2. Введите слово', 'Игра "Города"!')
        if player_2 is None:
            break
        choise2 = player_2
        if last_liters(choise1.lower()) == first_liters(player_2.lower()):
            if msgbox(f'Ваше слово должно начинаться с буквы: "{last_liters(player_2).upper()}"', 'Игра "Города"!')\
                    is None:
                break
            true_or_falce += 1
        elif last_liters(choise1.lower()) != first_liters(player_2.upper()):
            if msgbox(f'Игрок2 НЕВЕРНО!!!Ваше слово должно начинаться с буквы: "{last_liters(choise1).upper()}"',
                      'Игра "Города"!') is None:
                break

