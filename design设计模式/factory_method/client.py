#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/19'
__author__ = 'zhaohongyang'
"""

from factory_method.factory import drink_factory

tea_with_ice = drink_factory(origin_drink='tea', add='ice')
print(tea_with_ice.get_name())
print(tea_with_ice.get_price())