#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/19'
__author__ = 'zhaohongyang'
"""
from .drink import DrinkBase


class AddDecoratorBase(DrinkBase):

    def __init__(self, drink: DrinkBase) -> None:
        self.drink = drink


class IceDecorator(AddDecoratorBase):

    def get_price(self):
        return self.drink.get_price() + self.add_ice_price()

    def add_ice_price(self):
        price = 0.5
        return price

    def get_name(self):
        return self.drink.get_name() + '_with_' + self.add_ice_name()

    def add_ice_name(self):
        name = 'ice'
        return name


class SugerDecorator(AddDecoratorBase):

    def get_price(self):
        return self.drink.get_price() + self.add_suger_price()

    def add_suger_price(self):
        price = 0.5
        return price

    def get_name(self):
        return self.drink.get_name() + '_with_' + self.add_suger_name()

    def add_suger_name(self):
        name = 'suger'
        return name


class MilkDecorator(AddDecoratorBase):

    def get_price(self):
        return self.drink.get_price() + self.add_suger_price()

    def add_suger_price(self):
        price = 2
        return price

    def get_name(self):
        return self.drink.get_name() + '_with_' + self.add_suger_name()

    def add_suger_name(self):
        name = 'milk'
        return name
