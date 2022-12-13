# """Задача №1: Проверка корректности Имени"""
#
# str1 = input('Имя: ')
# if str1.isalpha() and str1.istitle():
#     print('Корректное имя')
# else:
#     print('Имя не коррректно')

# """Задача №2: Определить какой разряд числа больше"""
#
# num1 = int(input('Укажите число '))
# str_num = str(num1)
# if int(str_num[0]) > int(str_num[1]):
#     print('число старшего разряда больше')
# elif int(str_num[0]) < int(str_num[1]):
#     print('число младшего разряда больше')
# else:
#     print('числа разрядов равны')

# """Задача №3: Составление треугольника"""
#
# list_num = []
# num1 = int(input('длина отрезка1: '))
# list_num.append(num1)
# num2 = int(input('длина отрезка2: '))
# list_num.append(num2)
# num3 = int(input('длина отрезка1: '))
# list_num.append(num3)
# list_num.sort()
# if (list_num[0] == list_num[1]) and (list_num[2] == list_num[1]):
#     print('Равносторонний треугольник')
# elif (list_num[0]+list_num[1]) > list_num[2] and list_num[0] == list_num[1]:
#     print('Равнобедренный треугольник')
# elif (list_num[0]+list_num[1]) > list_num[2]:
#     print('Разносторонний треугольник')
# else:
#     print('Треугольник не выйдет')
#
#
#
#

# """Задача №4-5: Является ли слово палиндромом(должно читаться в обе стороны одинаково)"""
#
# str1 = input('Введите слово: ')
# if str1.lower() == str1.lower()[::-1]:
#     print('Cлово палиндром')
# else:
#     print('слово не палиндром')

# """Задача №6: Окончания слов """
#
# num1 = 0
# num2 = 0
# num3 = 0
# arrayTen = []  # масмв с исключкнниеми плюс 10
#
#
# def numberPlusTen():
#     for i in range(20, 1000, 10):
#         num1 = arrayTen.append(i + 2)
#         num2 = arrayTen.append(i + 3)
#         num3 = arrayTen.append(i + 4)
#
#
# numberPlusTen()
#
# num4 = 0
# num5 = 0
# num6 = 0
# arrayOneHungreet = []
#
#
# def numberPlusOneHungrit():
#     for i in range(110, 1000, 100):
#         num4 = arrayOneHungreet.append(i + 2)
#         num5 = arrayOneHungreet.append(i + 3)
#         num6 = arrayOneHungreet.append(i + 4)
#
#
# numberPlusOneHungrit()
#
# # Список для слова хомячка
# result = list(set(arrayTen) ^ set(arrayOneHungreet))
#
#
# def appendnumber(a):
#     result.append(a)
#
#
# appendnumber(2)
# appendnumber(3)
# appendnumber(4)
# # Список для слова хомячка
#
#
# while True:
#     number = int(input('Введите количество хомячков: '))
#
#     indexResult = 0
#     for i in result:
#         if i == number:
#             indexResult = True
#
#
#     def words(n):
#         if n % 2 == 1 and n != 11 and n % 10 == 1 and n % 100 != 11 or n == 1:
#             print(f'{n} хомячок')
#         elif indexResult:
#             print(f'{number} хомячка')
#         else:
#             print(f'{number} хомячков')
#
#
#     words(number)

# """Задача №7: Запрос имени пользователя"""
#
# name = 'admin'
# password = '123'
# str1 = input('Ваше имя: ')
# if str1.lower() == name:
#     try_num = 1
#     while try_num <= 3:
#         str2 = input('Пароль: ')
#         if str2 == password:
#             print(f'Добро пожаловать {name}!')
#             try_num = 3
#         else:
#             print(f'Неверный пароль! У вас осталось {3-try_num} попыток!')
#             try_num += 1
# else:
#     print(f'Добро пожаловать {str1.title()}!')

# """Задача №8: Проверка надежности пароля"""
#
# password = input('Пароль: ')
#
# if password.isalpha() or password.isnumeric():
#     print('password error')
# elif password.isupper() or password.islower():
#     print('password error')
# elif len(password) < 6:
#     print('password error')
# else:
#     print('good password')

"""Задача №9: Указать дату следующего дня"""

while True:
    num_day = int(input('Число: '))
    if num_day > 31 or num_day < 1:
        print('Не верное число')
        continue
    num_month = int(input('Месяц: '))
    if num_month > 12 or num_month < 1:
        print('Такого месяца нет')
        continue
    if num_day == 31 and num_month == 12:
        print(f'Число {1}, Месяц {1}')
    elif num_month == 2 and num_day > 28:
        print('В этом месяце 28 дней')
    elif ((num_month == 4 or num_month == 6) or (num_month == 9 or num_month == 11)) and num_day > 30:
        print('В этом месяце 30 дней')
    elif num_month == 2 and num_day == 28:
        print(f'Число {1}, Месяц {num_month + 1}')
    elif (num_month == 4 or 6 or 9 or 11) and num_day == 30:
        print(f'Число {1}, Месяц {num_month + 1}')
    elif (num_month == 1 or 3 or 5 or 7 or 8 or 10) and num_day == 31:
        print(f'Число {1}, Месяц {num_month+1}')
    else:
        print(f'Число {num_day+1}, Месяц {num_month}')
