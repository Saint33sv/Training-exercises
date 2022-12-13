import easygui
from random import randint


def set_file():
    int_user = easygui.fileopenbox()
    new_file = open(int_user, 'r')
    return set(new_file.read().split())


def count_file():
    int_user = easygui.fileopenbox()
    new_file = open(int_user, 'r')
    list_words = new_file.read().split()
    for i in set(list_words):
        dict_count = {i: list_words.count(i)}
        print(dict_count)


prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}


def compute_bill(dict_price):
    list_price = list(dict_price.values())
    return sum(list_price)


def xxx(num):
    """Подбор всех вариантов чисел сумма которых будет равна числу 'num'"""
    list_pluses = []
    for i in range(1, num):
        for a in range(1, num):
            if (i + a) == num:
                pluses = (i, a)
                list_pluses.append(pluses)
    return list_pluses


def igral_cub():
    cub1 = randint(1, 6)
    cub2 = randint(1, 6)
    print(f"""{cub1}: {xxx(cub1)}
{cub2}: {xxx(cub2)}""")







