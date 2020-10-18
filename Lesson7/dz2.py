from abc import ABC, abstractmethod


class Clothing(ABC):

    def __init__(self, value) -> None:
        self.__value = value

    @abstractmethod
    def tissue_consumption(self):
        return NotImplemented

    @property
    def value(self):
        return self.__value


class Coat(Clothing):

    def tissue_consumption(self):
        return self.value / 6.5 + 0.5


class Suit(Clothing):

    def tissue_consumption(self):
        return self.value * 2 + 0.3


print(sum([i.tissue_consumption() for i in [Coat(46), Suit(186), Coat(56), Suit(174), Coat(54), Suit(179)]]))
