from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def fabric_consumption(self):
        return round((self.size / 6.5) + 0.5, 2)


class Costume(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def fabric_consumption(self):
        return round((2 * self.height) + 0.3, 2)

# Не понятно, почему такой большой расход на пальто.
# Скорее всего тут должно быть не больше 4 м2.
сoat = Coat(50)
print(сoat.fabric_consumption)

costume = Costume(1.80)
print(costume.fabric_consumption)
