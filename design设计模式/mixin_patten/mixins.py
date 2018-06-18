#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/10'
__author__ = 'zhaohongyang'
"""


class IceMixin(object):

    def add_ice_price(self):
        price = 3
        return price

    def add_ice_name(self):
        name = 'ice'
        return name


class SugerMixin(object):

    def add_suger_price(self):
        price = 0.5
        return price

    def add_suger_name(self):
        name = 'suger'
        return name


class MilkMixin(object):

    def add_milk_price(self):
        price = 0.5
        return price

    def add_milk_name(self):
        name = 'suger'
        return name

