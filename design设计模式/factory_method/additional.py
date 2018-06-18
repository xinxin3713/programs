#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/10'
__author__ = 'zhaohongyang'
"""

import abc


class AddBase(metaclass=abc.ABCMeta):

    def add_price(self):
        return self.price

    def add_name(self):
        return self.name


class Ice(AddBase):

    name = 'ice'
    price = 0.3


class Suger(AddBase):

    name = 'suger'
    price = 0.5


if __name__ == '__main__':

    ice = Ice()

    print(ice.add_name())
