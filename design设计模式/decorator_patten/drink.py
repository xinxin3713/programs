#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/18'
__author__ = 'zhaohongyang'
"""


class DrinkBase(object):

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


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

