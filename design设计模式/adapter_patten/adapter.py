#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2018/1/10'
__author__ = 'zhaohongyang'
"""


class AdditionAdapter(object):

    def __init__(self, obj, adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)
        for key in self.__dict__:
            print(key,self.__dict__[key])
    #AdditionAdapter(ice, dict(add_name=ice.add_ice_name, add_price=ice.add_ice_price))
    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        for key in attr:
            print(key,self.__dict__[key])

        return getattr(self.obj, attr)

if __name__ =="__main__":
    pass