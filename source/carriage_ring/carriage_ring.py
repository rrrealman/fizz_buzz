
import random


class Carriage:

    __slots__ = '__light'

    def __init__(self, light=None):
        states = (0, 1)
        self.__light = bool(light or random.choice(states))

    def turn_light_on(self):
        self.__light = True

    def turn_light_off(self):
        self.__light = False

    @property
    def light_is_turned_on(self):
        return self.__light


class CarriageRing:

    def __init__(self, carriage_num=None):

        carriage_num = carriage_num or random.randint(50, 500)
        self.__carriages = [Carriage() for counter in range(carriage_num)]
        self.__current = 0

    @property
    def current_carriage(self):
        return self.__carriages[self.__current]

    def next(self):

        if self.__current == len(self.__carriages) - 1:
            self.__current = 0
        else:
            self.__current += 1

    def previous(self):

        if self.__current == 0:
            self.__current = len(self.__carriages) - 1
        else:
            self.__current -= 1
