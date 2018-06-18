#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/25'
__author__ = 'zhaohongyang'
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
   pass


if __name__ == '__main__':
    one = MyClass()
    two = MyClass()

    print(one == two)
    print(one is two)

    print(id(one), id(two))
