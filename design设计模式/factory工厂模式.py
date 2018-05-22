#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2017/9/11"

'''
Tea的 add_something(self,addcontion):方法就是桥接模式()
调用addcontion对象的接口

工厂模式就是把创建一个方法,tea和addcontion放在一起
运行接口,实现创建

'''
class AddContion(object):
    def __init__(self):
        self.name = None
        self.price =None

    def get_name(self):
        return self.name
    def get_price(self):
        return self.price

class Ice(object):
    def __init__(self):
        self.name = '冰'
        self.price = 1.0

class Suger (object):
    def __init__(self):
        self.name = "糖"
        self.price = 1.5

class Tea(object):
    def __init__(self,name,price):
        self.name= name
        self.price = price

    def get_name(self):
        return self.name
    def get_price(self):
        return self.price

    def add_something(self,addcontion):
        self.name += '加'+addcontion.name
        self.price += addcontion.price


def factory(drinks,addtion=None):
    drinks_class={'红茶':Tea('红茶',4),'凉茶':Tea('凉茶',5),'加多宝':Tea('加多宝', 6)}
    addtion_class={'ice':Ice,'suger':Suger}

    if drinks not in drinks_class:
        return '没有这种饮料'
    drink = drinks_class.get(drinks)

    if addtion:
        add = addtion_class.get(addtion)()
        drink.add_something(add)

    print(drink.get_name(),drink.get_price())

if __name__ == '__main__':

    factory('红茶','ice')
    factory('加多宝')
    factory('凉茶','suger')
