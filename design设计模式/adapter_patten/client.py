#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/20'
__author__ = 'zhaohongyang'
"""

from drink import Tea
from additional import Ice
from adapter import AdditionAdapter

tea = Tea()
ice = Ice()

tea.add_something(AdditionAdapter(ice, dict(add_name=ice.add_ice_name, add_price=ice.add_ice_price)))
#tea.add_something(ice)
print(tea.get_name())
print(tea.get_price())