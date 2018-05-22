#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2017/9/10"

'''
两个类之间的方法名不匹配,用适配器模式
一般是后来改的时候,没办法才用的
'''

#1 添加剂类,有不同的添加剂
#设置一个基类,其他的继承 ,
class Addition(object):
    def __init__(self,name,price):
        self.name = name
        self.pirce =price

class Ice(Addition):

    def __init__(self):
        self.name ='冰'
        self.price =1

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    # def get_id(self):
    #     return self.price

class Suger(Addition):

    def __init__(self):
        self.name = '糖'
        self.price = 1.5

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

#2 饮料类, 茶,咖啡

class Drinks(object):

    def __init__(self,name,price):

        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def add_someting(self,obj):
        self.name  += '加'+obj.add_name()
        self.price += obj.add_price()

class Tea(Drinks):

    def __init__(self,name,price):
        self.name = name
        self.price = price

class Coffee(Drinks):

    def __init__(self,name,price):
        self.name = name
        self.price = price



'''
因为Drinks类添加Ice对象,它的方法名不是add_name()

    def add_someting(self,obj):
        self.name  += '加'+obj.add_name()
        self.price += obj.add_price()
Ice类的实例方法       
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price  

所以需要有个适配器类

'''
#适配器类
class AdditionAdapter(object):

    def __init__(self,obj,adapted_methods):
        #把需要改动的对应参数名字写到__dict__作用(用来保存所用到的参数,变量,方法名)
        self.obj =obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, item):
        #如果找不到就会去__dict__里找
        return getattr(self.obj,item)

if __name__ == '__main__':

    tea = Tea('红茶',8)
    ice = Ice()
    tea.add_someting(AdditionAdapter(ice,dict(add_name=ice.get_name,add_price=ice.get_price)))

    print(tea.get_name(),tea.get_price())