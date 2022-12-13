class Couter(object):
    def __init__(self):
        self.__cur_value = 0

    def get_couter(self):
        return self.__cur_value

    def increment(self):
        self.__cur_value += 1
        if self.__cur_value > 9:
            self.__cur_value = 0

    def decrement(self):
        self.__cur_value -= 1
        if self.__cur_value < 0:
            self.__cur_value = 9


C = Couter()
for i in range(20):
    print(C.get_couter())
    C.decrement()
print(C.get_couter())
