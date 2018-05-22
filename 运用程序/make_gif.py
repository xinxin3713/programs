#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/4/8"


# import imageio,os
# images = []
#
#
# images.append(imageio.imread('1.jpg'))
# images.append(imageio.imread('2.jpg'))
# images.append(imageio.imread('3.jpg'))
# imageio.mimsave('gif.gif', images,duration=1)
s = "abc中国"
# 对字符进行编码，参数用来指定编码方式。默认为UTF-8。
# for item in s:
#     print(ord(item))
#
# b = s.encode()
# print(b)
# for item in b:
#     print(item)
# # 对字节类型调用decode方法，可以进行解码为字符类型。
# # 将字节类型恢复成字符类型。参数指定编码方式。默认为UTF-8。
# s = b.decode("UTF-8")
# print(s)
#
# # 编码与解码也可以使用bytes与str函数。
# b = bytes(s, "utf-8")
# print(b)
# s = str(b, "utf-8")
# print(s)
def lengthOfLongestSubstring(s,li =[]):
    """
    :type s: str
    :rtype: int
    """
    if s == find_same(s):
        li.append(s)
        return li
    else:


        frond,back,=find_same(s)
        li.append(frond)
        lengthOfLongestSubstring(back,li)
        return li


def  find_same(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            for j in range(i+1,len(s)):
                if s[i]!=s[j]:
                    return (s[:i+1],s[j:] )
    return  s






result=[]
s = lengthOfLongestSubstring('asddfessabedf',result)
print(s)
print(max(list(map(len,s))))

# a,b =find_same('asddfessabedf')
# a,b = find_same(b)
# print(a,b)
# a = find_same(b)
# print(a,b)
