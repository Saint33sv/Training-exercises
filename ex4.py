# """Задача №1: Добавление элементов в список"""
#
# colors = []
# for i in range(4):
#     get_color = input("Укажите цвет: ")
#     colors.append(get_color)
# print(colors)

# """Задача №2: Объединить два списка без повторений элементов"""
#
# list_a = [1, 23, 4, 45, 3, 6]
# list_b = [2, 3, 34, 6, 66, 77]
# list_a.extend(list_b)
# list_a.pop(4)
# list_a.pop(4)
# print(f"{list_a}, количество элементов {len(list_a)}")

# """Задача №3: Сочетание и Произведение элементов списка"""
# list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#
# def combination_multiplication(ex_list):
#     com_num = 0
#     mul_num = 1
#     for i in ex_list:
#         com_num += i
#         mul_num *= i
#     print(f"Сумма элементов {com_num}, произведение элементов {mul_num}")
#
#
# combination_multiplication(list_a)

# """Задача №4: Нарисовать квадрат с различными цветами граней"""
# from turtle import *
# color_list = ['green', 'red', 'yellow', 'orange']
# shape('turtle')
#
#
# for i in range(4):
#     color(color_list[i])
#     fd(200)
#     lt(90)
#
# done()

"""Задача №5: Сортировка списка методом пузырька"""
from random import randint
N = 10
list_a = [randint(1, 100)for i in range(N)]  # Рандомное заполнение списка
print(list_a)


def bubble(ex_list):
    for i in range(N-1):
        for j in range(N-1-i):
            if ex_list[j] > ex_list[j+1]:
                ex_list[j], ex_list[j+1] = ex_list[j+1], ex_list[j]
    print(ex_list)


bubble(list_a)
