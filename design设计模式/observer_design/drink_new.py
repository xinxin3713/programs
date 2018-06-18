#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/16'
__author__ = 'zhaohongyang'
"""


class Tea(object):
    """Class Tea"""

    def __init__(self):
        self.name = 'Tea'
        self.price = 2
        self.__subscribers = []

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    # 提供注册
    def attch(self, subscriber):
        self.__subscribers.append(subscriber)

    # 更新价格
    def update_price(self, price):
        self.price = price
        for sub in self.__subscribers:
            sub.update_tea_price(self.price)


class Ice(object):
    """ ice """

    def __init__(self):
        self.name = 'ice'
        self.price = 1
        self.__subscribers = []

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    # 提供注册
    def attch(self, subscriber):
        self.__subscribers.append(subscriber)

    # 更新价格
    def update_price(self, price):
        self.price = price
        for sub in self.__subscribers:
            sub.update_ice_price()


class TeaWithIce(object):

    def __init__(self, tea, ice):
        self.tea = tea
        self.ice = ice
        self.tea.attch(self)
        self.ice.attch(self)

        self.ice_name = 'ice'
        self.tea_name = 'tea'
        self.ice_price = 1
        self.tea_price = 2

    def get_price(self):
        return self.ice_price + self.tea_price

    def get_name(self):
        return self.ice_name + 'with' + self.tea_name

    def update_ice_price(self):
        self.ice_price = self.ice.get_price()

    def update_tea_price(self, price):
        self.tea_price = self.tea.get_price()

if __name__ == '__main__':

    tea = Tea()
    ice = Ice()

    tea_with_ice = TeaWithIce(tea, ice)

    print(tea_with_ice.get_price())

    tea.update_price(price=5)
    print(tea.get_price())
    print(tea_with_ice.get_price())
