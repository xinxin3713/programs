#!/usr/bin/env/python3
# -*- coding:utf-8 -*-
"""
__creater__"2018-1-27"
__author__'LiuXin'
"""
from functools import wraps
import time

def exe_run_time(fun):
    """
    执行时间装饰器
    :param fun:
    :return:
    """
    @wraps(fun)
    def inner(*args, **kwargs):
        t0 = time.time()
        result = fun(*args, **kwargs)
        run_time = time.time() - t0
        name = fun.__name__
        str_out = []
        if args:
            str_out.append(','.join(repr(arg) for arg in args))
        if kwargs:
            key_value = [f'{k}={v}' for (k, v) in kwargs.items()]
            str_out.append(','.join(key_value))
        out_print = ','.join(str_out)

        print("{:0.8f}".format(run_time), f"{name}({out_print})--->{result}")
        return result

    return inner
if __name__=="__main__":
    @exe_run_time
    def ff(s, a=1):
        for i in range(100000):
            i = 1
        return (s + a)
    print(ff.__closure__)
    print(ff.__code__.co_argcount)
    print(ff.__code__.co_varnames)
    print(ff.__dict__)
    ff(38,a=88)

