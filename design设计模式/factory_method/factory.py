#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/11'
__author__ = 'zhaohongyang'
"""

from factory_method.drink import Tea, Coffee
from factory_method.additional import Ice, Suger


def drink_factory(origin_drink, add=None):
    origin_drink_to_class = {
        'tea': Tea,
        'coffee': Coffee,
    }
    add_to_class = {
        'ice': Ice,
        'suger': Suger,
    }

    if origin_drink not in origin_drink_to_class:
        return 'error'

    o_d = origin_drink_to_class[origin_drink]()
    if add and add in add_to_class:
        add_d = add_to_class[add]()
        o_d.add_something(add_d)

    return o_d
