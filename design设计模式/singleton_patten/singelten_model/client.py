#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/25'
__author__ = 'zhaohongyang'
"""

from singleton_patten.singelten_model.singlenton_class import my_singleton
from singleton_patten.singelten_model.singlenton_class import MySingleton

print(my_singleton.id)

one = MySingleton()
two = MySingleton()

print(one == two)
print(one is two)

print(id(one), id(two))
