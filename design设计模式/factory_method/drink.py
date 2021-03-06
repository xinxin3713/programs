#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/10'
__author__ = 'zhaohongyang'
"""


import abc


class DrinkBase(metaclass=abc.ABCMeta):

    def __init__(self):
        self.name = ''
        self.price = 0

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def add_something(self, add):
        self.name += '_with_' + add.add_name()
        self.price += add.add_price()


class Tea(DrinkBase):

    def __init__(self):
        super(Tea, self).__init__()
        self.name = 'tea'
        self.price = 2


class Coffee(DrinkBase):

    def __init__(self):
        super(Coffee, self).__init__()
        self.name = 'coffee'
        self.price = 3


class Milk(DrinkBase):
    """Class Milk"""

    def __init__(self):
        super(Milk, self).__init__()
        self.name = 'milk'
        self.price = 3


class Water(DrinkBase):
    """Class Water"""

    def __init__(self):
        super(Water, self).__init__()
        self.name = 'water'
        self.price = 1


class Fanta(DrinkBase):

    def __init__(self):
        super(Fanta, self).__init__()
        self.name = 'fenta'
        self.price = 4


if __name__ == '__main__':

    fenda = Fanta()

    print(fenda.get_name())

