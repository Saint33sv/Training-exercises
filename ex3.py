from turtle import *

# """Задача №1: Проверка числа"""
# while True:
#     number = int(input('Введите число:> '))
#
#     if number < 0:
#         print("Число отрицательное!")
#     elif number > 0:
#         print("Число положительное!")
#     else:
#         print("Число равно нулю!")

# """Задача №2: логическое И"""
# age = int(input('Укажите свой возраст:> '))
# experience = int(input('Укажите свой стаж:> '))
# if age >= 20 and experience >= 3:
#     print('Вы нам подходите')
# else:
#     print("Вы нам не подходите")

"""Задача №3: движение черепашки"""


def right_():
    seth(0)
    fd(50)


def left_():
    seth(180)
    fd(50)


def up_():
    seth(90)
    fd(50)


def down_():
    seth(270)
    fd(50)


question1 = input("Укажите направление вверх, вниз, влево, вправо: ")
question2 = input("Укажите направление вверх, вниз, влево, вправо: ")
question3 = input("Укажите направление вверх, вниз, влево, вправо: ")
question4 = input("Укажите направление вверх, вниз, влево, вправо: ")
question5 = input("Укажите направление вверх, вниз, влево, вправо: ")
question6 = input("Укажите направление вверх, вниз, влево, вправо: ")
oll_questions = [question1, question2, question3, question4, question5, question6]
shape('turtle')
for i in oll_questions:
    if i == "вверх":
        up_()
    elif i == "вниз":
        down_()
    elif i == "влево":
        left_()
    elif i == "вправо":
        right_()
    else:
        print("Команда не существует")


done()

# """Задача №4: Определить пору года по номеру месяца"""
# while True:
#     num_month = int(input("Номер месяца: "))
#
#     if (num_month == 3) or (num_month == 4) or (num_month == 5):
#         print("Весна")
#
#     elif (num_month == 6) or (num_month == 7) or (num_month == 8):
#         print("Лето")
#
#     elif (num_month == 9) or (num_month == 10) or (num_month == 11):
#         print("Осень")
#
#     elif (num_month == 12) or (num_month == 1) or (num_month == 2):
#         print("Зима")
#     else:
#         print("Такого месяца нет")
