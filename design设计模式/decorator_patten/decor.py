#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/10'
__author__ = 'zhaohongyang'
"""
import functools

class Suger(object):

    __name = 'suger'
    __price = 0.5

    @classmethod
    def add_suger_price(cls, func):
        @functools.wraps(func)
        def get_new_price(*args, **kwargs):
            origin_price = func(*args, **kwargs)
            new_price = cls.__price + origin_price
            return new_price

        return get_new_price

    @classmethod
    def add_suger_name(cls, func):
        @functools.wraps(func)
        def get_new_name(*args, **kwargs):
            origin_name = func(*args, **kwargs)
            new_name = origin_name + '_with_' + cls.__name
            return new_name

        return get_new_name


class Tea(object):
    def __init__(self):
        self.__name = 'Tea'
        self.__price = 2

    @Suger.add_suger_price
    def get_price(self):
        return self.__price

    @Suger.add_suger_name
    def get_name(self):
        return self.__name

if __name__ == '__main__':
    tea = Tea()
    print(tea.get_price())
    print(tea.get_name())
    print(tea.get_price())
    print(tea.get_name())