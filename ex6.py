# """Задача №1-№2: Фамилия и инициалы"""
#
# str1 = input('Фамилия: ')
# str2 = input('Имя: ')
# str3 = input('Отчество: ')
# print(f'{str1.title()} {str2.title()[0]}. {str3.title()[0]}.')

# """Задача №3: Подсчет количества входящего елемента в строку"""
#
# str1 = input('Введите строку: ')
# print(f"В данной строке {str1.count('а')} букв 'а' ")

# """Задача №4: Замена старой подстроки на новую"""
#
# str1 = input('Введите строку: ')
# str2 = input('Что хотите заменить: ')
# str3 = input('На что хотите заменить: ')
# print(str1)
# print(str1.replace(str2, str3))

# """Задача №5: Замена буквы "ё" на букву "е"."""
#
# str1 = input("Введите строку: ")
# print(str1.replace('ё', 'е'))

# """Задача №6: Удалить первое слово в строке"""
#
# str1 = input('Введите cтроку: ')
# list_str1 = str1.split()
# list_str1.pop(0)
# print(' '.join(list_str1))

# """Задача №7: Удалить последнее слово в строке"""
#
# str1 = input('Введите строку: ')
# list_str1 = str1.split()
# list_str1.pop(-1)
# print(' '.join(list_str1))

# """Задача №8: Поменять слова местами"""
#
# str1 = input('Введите строку: ')
# list_str1 = str1.split()
# list_str1.reverse()
# print(' '.join(list_str1))

# """Задача №9: Транслитерация введенного слова"""
# from transliterate import translit
# str1 = input('Введите строку: ')
# print(translit(str1, reversed=True))

