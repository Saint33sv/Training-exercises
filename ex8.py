# """Задача №1-2: Вывести числа в диапазоне не включая значения + вывести числа с делением на 5 без остатка"""
#
# num1 = int(input('Число 1:'))
# num2 = int(input('Число 2: '))
# list_nums = []
#
# for i in range(num1+1, num2):
#     if i % 5 == 0:
#         list_nums.append(i)
# print(list_nums)

# """Задача №3: Вывести таблицу умножения на указаное число"""
#
# num1 = int(input('Укажите число'))
# for i in range(1, 11):
#     print(f"{num1}*{i}={num1*i}")

# """Задача №4: Вопросы в цыкле"""
# sum_ = []
# exams = ['Экзамен1', 'Экзамен2', 'Экзамен3', 'Экзамен4']
# for i in exams:
#     num1 = int(input(f'Укажите оценку за {i}: '))
#     sum_.append(num1)
# print(sum(sum_))

# """Задача №5: Бесконечный цыкл и вывод суммы введенных чисел"""
# l_n = []
#
# while True:
#     num1 = input('Введите число:')
#     if num1 == 'end':
#         break
#     l_n.append(int(num1))
# print(sum(l_n))

# """Задача №6: Посчитать сумму цифр в числе"""
#
# num1 = int(input('Введите число: '))
# num = str(num1)
# a = 0
# l_n = []
# while a <= len(num)-1:
#     num2 = num[a]
#     l_n.append(int(num2))
#     a += 1
# print(sum(l_n))

# """Задача №7: Определить сколько раз цифра 'a' входит в число 'x'"""
#
# num = int(input('Укажите число '))
# num1 = int(input('Укажите цифру '))
# s_num = str(num)
# s_num1 = str(num1)
# a = 0
# for i in range(len(s_num)):
#     if s_num[i] == s_num1:
#         a += 1
# print(a)









