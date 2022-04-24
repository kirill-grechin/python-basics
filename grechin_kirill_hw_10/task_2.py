from abc import ABC, abstractmethod


# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
# знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
# декоратора @property.


class Clothes(ABC):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def calculate_fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.__size = size

    def calculate_fabric_consumption(self):
        return self.__size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, growth):
        super().__init__(name)
        self.__growth = growth

    def calculate_fabric_consumption(self):
        return 2 * self.__growth + 0.3


coat = Coat('Representative coat', 44)
print(coat.name, coat.calculate_fabric_consumption(), sep=' ')
suit = Suit('Business suit', 48)
print(suit.name, suit.calculate_fabric_consumption(), sep=' ')
