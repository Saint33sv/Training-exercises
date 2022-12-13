from random import randint


class Student(object):
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = {"Химия": randint(1, 5), "Физика": randint(1, 5), "Математика": randint(1, 5), "История": randint(1, 5)}

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age}"

    def greet(self):
        print(f"Привет! Меня зовут {self.surname} {self.name}, мне {self.age}")

    def average_score(self):
        return float(sum(self.grades.values())/len(self.grades.values()))


student1 = Student("Иван", "Петров", "18 лет")
student2 = Student("Коля", "Иванов", "15 лет")
student3 = Student("Василий", "Сидоров", "11 лет")
student4 = Student("Хуй", "С бугра", "45 лет")
list_stud = []
s = {}
list_stud.append(student1)
list_stud.append(student2)
list_stud.append(student3)
list_stud.append(student4)
for i in range(len(list_stud)-1):
    for j in range(len(list_stud)-1):
        if list_stud[j].average_score()<list_stud[j+1].average_score():
            list_stud[j], list_stud[j+1] = list_stud[j+1], list_stud[j]
for i in list_stud:
    s[i.__str__()] = i.average_score()
print(s)
