#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/25'
__author__ = 'zhaohongyang'
"""


class SpamMeta(type):

    def __init__(cls, *args, **kwargs):
        print("SpamMeta __init__")
        super(SpamMeta, cls).__init__(*args, **kwargs)

    def __new__(mcs, *args, **kwargs):
        print('SpamMeta __new__')
        return super(SpamMeta, mcs).__new__(mcs, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('SpamMeta __call__')
        return super(SpamMeta, cls).__call__(*args, **kwargs)


class Spam(metaclass=SpamMeta):
    def __init__(self, *args, **kwargs):
        print("Spam __init__")
        super(Spam, self).__init__(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        print('Spam __new__')
        return super(Spam, cls).__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print('Spam __call__')
        return super(Spam, self).__call__(*args, **kwargs)

    @staticmethod
    def grok(x):
        print('Spam.grok')


if __name__ == '__main__':
    print('1========================================')
    spam = Spam()
    print('2========================================')
    spam2 = Spam()
    print('3========================================')
    spam.grok('a')

