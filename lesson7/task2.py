#!/usr/bin/env python3

"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
проекта, проверить на практике работу декоратора @property. """


from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    @abstractmethod
    def calc_textile(self):
        pass

    @property
    def textile(self):
        return round(self.calc_textile(), 2)


class Coat(AbstractClothes):
    size: int

    def __init__(self, size):
        self.size = size

    def calc_textile(self):
        return self.size / 6.5 + .5


class Suit(AbstractClothes):
    height: int

    def __init__(self, height):
        self.height = height

    def calc_textile(self):
        return self.height * 2 + .3


class CompositeClothes(AbstractClothes):
    def __init__(self, items: list):
        self.items = items

    def calc_textile(self):
        return sum([item.textile for item in self.items])


coat = Coat(30)
suite = Suit(32)
print(coat.textile)
print(suite.textile)

composite = CompositeClothes([coat, suite])
print(composite.calc_textile())
