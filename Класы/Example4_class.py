from time import sleep


class Watch(object):
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def get_watch(self):
        return f"{self.__hour}:{self.__minute}:{self.__second}"

    def add_second(self):
        self.__second += 1
        if self.__second > 59:
            self.__second = 0
            self.add_minute()

    def add_minute(self):
        self.__minute += 1
        if self.__minute > 59:
            self.__minute = 0
            self.add_hour()

    def add_hour(self):
        self.__hour += 1
        if self.__hour > 23:
            self.__hour = 0

    def __add__(self, ho, min, sec):
        for h in range(ho):
            self.add_hour()
        for m in range(min):
            self.add_minute()
        for s in range(sec):
            self.add_second()
        return f"{self.__hour}:{self.__minute}:{self.__second}"

W = Watch(16, 59, 55)
print(W.__add__(5, 5, 5))
