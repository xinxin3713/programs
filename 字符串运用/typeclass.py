#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
__created__='2018/1/27'
__author__ = 'LiuXin'
"""
class MyMeta(type):

    def __init__(cls, name, base, attr):
        print('22')
        print('cls', cls, name, base)
        print(attr)
        super(MyMeta, cls).__init__(name, base, attr)

    def __new__(mcs, name, base, attr):
        print(11)
        print("mcs", mcs, name, base)
        print(attr)
        return super(MyMeta, mcs).__new__(mcs, name, base, attr)

    def __call__(cls, *args, **kwargs):
        print(33)
        print("__call__", cls)
        print(super(MyMeta, cls).__call__(*args, **kwargs))
        return super(MyMeta, cls).__call__(*args, **kwargs)


class MyClass(metaclass=MyMeta):
    def __new__(cls, *args, **kwargs):
        print(1)
        return super(MyClass, cls).__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print(self)
        print(3, 'MyClass__call__')

    def __init__(self, *args, **kwargs):
        print(2)
        super(MyClass, self).__init__(*args, **kwargs)

    @staticmethod
    def pock():
        print("pock")


if __name__ == '__main__':
    myclass = MyClass()
    print("===============================")
    myclass2 = MyClass()
    print('=================================')
    myclass()
