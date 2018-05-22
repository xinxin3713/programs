#!/usr/bin/env python
# _*_coding:utf-8 _*_
import functools

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2017/9/10"

class Ice(object):
    name = "冰"
    price=1.0

class Suger (object):
    name = "糖"
    price=1.5


class AddCondition(object):

    @classmethod
    def add_price(cls, price):
        def middle(func):
            @functools.wraps(func)
            def inner(*args, **kwargs):
                old_price = func(*args, **kwargs)
                new_price = old_price + price
                return new_price
            return inner
        return middle


    @classmethod
    def add_name(cls, name):
        def middle(func):
            @functools.wraps(func)
            def inner(*args, **kwargs):
                old_price = func(*args, **kwargs)
                new_price = old_price +'加'+ name
                return new_price
            return inner
        return middle

class Tea(object):

    def __init__(self,name,price,addcontion = None):
        self.name = name
        self.price = price
        self.addcontion = addcontion


    def get_name(self):
        if self.addcontion==None:
            return self.name
        elif self.addcontion == Ice.name:
            return self.get_add_ice_name()
        elif self.addcontion == Suger.name:
            return self.get_add_suger_name()



    @AddCondition.add_name(name=Ice.name)
    def get_add_ice_name(self):
        return self.name
    @AddCondition.add_price(price=Suger.price)
    def get_add_ice_price(self):
        return self.price
    @AddCondition.add_name(name=Suger.name)
    def get_add_suger_name(self):
        return self.name
    @AddCondition.add_price(price=Ice.price)
    def get_add_suger_price(self):
        return self.price


if __name__=='__main__':
    tea = Tea('绿茶', 5, '冰')
    print(tea.get_name())


