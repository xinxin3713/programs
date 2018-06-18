#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/5/7"

#汉若塔
def hanruota(A,B,C,n):
    if n ==1:
        print(f'{A}->{C}')
    else:
        hanruota(B,C,A,n-1)
        print(f'{A}->{C}')
        hanruota(B,A,C,n-1)
hanruota('a','b','c',3)
#输出目录下的所有文件
import os
def print_files(path):
    if os.path.isfile(path):
        print(path)
    else:
        chileds = os.listdir(path)
        for chiled in chileds:
            chiled_path = os.path.join(path,chiled)
            print_files(chiled_path)

def print_files2(path):
    childs =os.listdir(path)
    for child in childs :
        child_path =os.path.join(path,child)
        if os.path.isdir(child_path):
            print_files2(child_path)
        else:
            print(child_path)

print_files('E:\DjangoBlog')
print_files2('E:\DjangoBlog')

#输出含多个嵌套列表

def print_list(li):
    for item in li:
        if isinstance(item, (list, tuple)):
            print_list(item)
        else:
            print(item)

li =[[123,['12as','ddad'],123],('112','yu',[12,33,[44,55]])]
print_list(li)
#矩阵转置
li = [[1,2,3],
      [4,5,6]]
li_t = [[item[n] for item in li] for n in range( len(li[0]))]
print(li_t)
# m中任选n个的组合

def combination(s,n):
    if n ==1:
        return list(s)
    elif n == len(s):
        return [s]
    else:
        result= []
        #先把第一个字符的所有匹配的输出
        pre = combination(s[1:],n-1)
        for item in pre:
            result.append(s[0]+item)
        #然后把第二个到m-n的都加上
        result.extend(combination(s[1:],n))
        return result

print(len(combination("abcde", 3)))

# m中任选n个的排列

def permutation(s,n):
    if n ==1:
        return list(s)

    else:
        result = []
        per = permutation(s[1:],n-1)
        for item in per:
            for i in range(0,len(item)+1):
                result.append(item[:i]+s[0]+item[i:])
        if len(s)>n:
            result.extend(permutation(s[1:], n))
        return result

print(len(permutation("abcde",3)))

