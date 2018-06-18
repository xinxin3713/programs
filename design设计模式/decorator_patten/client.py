#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/19'
__author__ = 'zhaohongyang'
"""

from .drink import Tea
from .decorator import IceDecorator, SugerDecorator


tea_with_ice_and_suger = SugerDecorator(IceDecorator(Tea()))

print(tea_with_ice_and_suger.get_name())
print(tea_with_ice_and_suger.get_price())
