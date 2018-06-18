#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/19'
__author__ = 'zhaohongyang'
"""

from bridge_patten.drink import Tea
from bridge_patten.additional import Ice


tea = Tea()
ice = Ice()
tea.add_something(ice)
print(tea.get_name())
print(tea.get_price())
