from cities import cities_list
from random import choice
from easygui import *


def one_player():
    variants_comp = []
    use_words = []
    start_game = True
    choice_comp = str()
    while True:
        player = enterbox(msg='Укажите город!', title="Игра 'Города'")
        if player is None:
            break
        for a in use_words:
            if player.lower() == a:
                if msgbox(f"Этот город уже был! Город на букву '{choice_comp[-1]}'!", "Игра 'Города'") is None:
                    break
                continue

        if cities_list.count(player.lower()) > 0 and (start_game or player.lower()[0] == choice_comp[-1]):
            for i in cities_list:
                if player.lower()[-1] == i[0]:
                    variants_comp.append(i)
            choice_comp = choice(variants_comp)
            use_words.append(player.lower())
            use_words.append(choice_comp)
            if msgbox(msg=f"{choice_comp.title()} город на букву '{choice_comp[-1]}'!", title="Игра 'Города'") is None:
                break
            variants_comp.clear()
            start_game = False
        else:
            if msgbox(f"Такого города нет в базе или город указан не с той буквы! Город на букву '{choice_comp[-1]}'!",
                      "Игра 'Города'") is None:
                break


def two_player():

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
            if msgbox(f'Ваше слово должно начинаться с буквы: "{last_liters(player_1).upper()}"', 'Игра "Города"!') \
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
                if msgbox(f'Ваше слово должно начинаться с буквы: "{last_liters(player_2).upper()}"', 'Игра "Города"!') \
                        is None:
                    break
                true_or_falce += 1
            elif last_liters(choise1.lower()) != first_liters(player_2.upper()):
                if msgbox(f'Игрок2 НЕВЕРНО!!!Ваше слово должно начинаться с буквы: "{last_liters(choise1).upper()}"',
                          'Игра "Города"!') is None:
                    break


ind_num = ['Один игрок', 'Два игрока']
game_num = [one_player, two_player]

while True:
    play = buttonbox(msg='Количество игроков', title='Игра "Города"!', choices=ind_num, image='../games/putin.png')
    if play is None:
        break
    game_num[ind_num.index(play)]()

