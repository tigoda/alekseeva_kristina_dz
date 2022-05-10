from abc import ABC, abstractmethod


class Clothes(ABC):
    consumption = 0

    def __init__(self, v, h):
        self.v = v
        self.h = h

    @abstractmethod
    def coat_v(self):
        pass

    @abstractmethod
    def suit_h(self):
        pass

    @property
    def coat_and_suit(self):
        return f'Пальто:{self.v}. Костюм:{self.h}. Общий расход ткани: {self.consumption:.2f}'


class Coat_suit(Clothes):
    def coat_v(self):
        coat = self.v / 6.5 + 0.5
        Clothes.consumption += coat
        print(f'Пальто:{coat :.2f}')

    def suit_h(self):
        suit = 2 * self.h + 0.3
        Clothes.consumption += suit
        print(f'Костюм:{suit :.2f} ')


a = Coat_suit(30, 90)
a.coat_v()
a.suit_h()
print(a.coat_and_suit)

b = Coat_suit(300, 800)
b.coat_v()
b.suit_h()
print(b.coat_and_suit)
