from time import sleep


class Herbivore:
    def __init__(self):
        self.__satiety = 10

    def saturation(self):
        grass = Grass().get_caloric()
        while self.__satiety != 0:
            self.__satiety -= 1
            print("Животное не голодно!")
            sleep(1)
        print("Животное проголодалось!")
        while self.__satiety != 10:
            print("Животное ест...")
            self.__satiety += grass
            sleep(1)
        print("Животное сытое!")


class Grass:
    def __init__(self):
        self.__caloric = 1

    def get_caloric(self):
        return self.__caloric

animal = Herbivore()
while True:
    animal.saturation()
