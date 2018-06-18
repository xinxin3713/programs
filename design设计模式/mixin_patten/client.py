#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/18'
__author__ = 'zhaohongyang'
"""

from mixin_patten.drink import Tea, Coffee
from mixin_patten.mixins import IceMixin, MilkMixin, SugerMixin


class TeaWithIce(IceMixin, Tea):

    def get_name(self):
        return super(TeaWithIce, self).get_name() + '__with__' + self.add_ice_name()

    def get_price(self):
        return super(TeaWithIce, self).get_price() + self.add_ice_price()


class CoffeeWithMilk(MilkMixin, Coffee):

    def get_name(self):
        return super(CoffeeWithMilk, self).get_name() + '__with__' + self.add_milk_name()

    def get_price(self):
        return super(CoffeeWithMilk, self).get_price() + self.add_milk_price()


class CoffeeWithIceAndSuger(MilkMixin, IceMixin, Coffee):

    def get_name(self):
        return super(CoffeeWithIceAndSuger, self).get_name() + '__with__' + self.add_milk_name() + '_and_' + self.add_ice_name()

    def get_price(self):
        return super(CoffeeWithIceAndSuger, self).get_price() + self.add_milk_price() + self.add_ice_price()


if __name__ == '__main__':

    tea_with_ice = TeaWithIce()
    print(tea_with_ice.get_name())
