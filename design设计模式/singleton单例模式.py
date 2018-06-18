#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2017/9/10"
"""
1,import模块
2,继承,通过 __new__(cls, *args, **kwargs):来创建类的每次都创建同一个类
,然后再执行__init__是用来创建类对象的
"""
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if  not cls._instance :
            cls._instance = super(Singleton,cls).__new__(cls,*args, **kw)
        return cls._instance



class MyClass(Singleton):
    a =1
'''
3,元类 通过调用类创建时用()调用__call__当来限制
'''
# class Singleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls]= super(Singleton,cls).__call__(*args,**kwargs)
#         return cls._instances[cls]

# class MyClass(metaclass=Singleton):
#     a = 1

# import threading
#
#
# class Singleton(object):
#     __instant = None;
#     __lock = threading.Lock();
#
#     def __new__(self):
#         print("111 new")
#         if (Singleton.__instant == None):
#             Singleton.__lock.acquire();
#             if (Singleton.__instant == None):
#                 print("001 create")
#                 Singleton.__instant = object.__new__(self);
#             Singleton.__lock.release()
#         return Singleton.__instant
#
#     def __init__(self):
#         print("0000 init")
#         self.name = "111"
#
#
# if __name__ == '__main__':
#
#     s1 = Singleton()
#     s2 = Singleton()
#
#     print(s1.name)
#     print(s2.name)
#     s1.name = '222'
#     print(id(s1), id(s2))
#     print(s2.name)
#

if __name__=="__main__":
    one =MyClass()
    two =MyClass()
    print(one == two)
    print(one is two)
    print(id(one),id(two))