#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/25'
__author__ = 'zhaohongyang'
"""


class Singleton(type):

    instance = {}

    def __new__(mcs, *args, **kw):
        if not mcs.instance:
            mcs.instance[mcs] = super(Singleton, mcs).__new__(mcs, *args, **kw)
        return mcs.instance[mcs]


class MyClass(metaclass=Singleton):
    a = 1


if __name__ == '__main__':

    one = MyClass()
    two = MyClass()

    print(one == two)
    print(one is two)

    print(id(one), id(two))
