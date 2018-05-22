#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2017/1/10'
__author__ = 'liuxin'
"""
# 在屏幕上显示跑马广告词
import os
import time


def guan_gao(text):
    content = text
    while True:
        # 清理屏幕上的输出
        os.system("cls")
        print(content)
        time.sleep(1)
        content = content[1:] + content[0]
#统计列表中元素出现的次数
li = [1,2,5,3,3,2,2,6,6,2]
count_dict={}
for item in li :
    count_dict[item]=count_dict.get(item,0)+1
count_dict.setdefault(7,7)
print(count_dict)

# -----------------------------------------------------------------
# 设计一个4为验证码,有小写字母和数字构成
import random


def generate_code(code_len=4):
    all_chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
    code = ""
    for _ in range(code_len):
        index = random.randrange(0, len(all_chars) - 1)
        code += all_chars[index]
    return code


# -----------------------------------------------------------------
# 设计一个返回文件后缀名的函数
def get_suffix(file_name, has_dot=False):
    pos = file_name.rfind('.')
    if 0 < pos < len(file_name):
        index = pos if has_dot else pos + 1
    return file_name[index:]


# -----------------------------------------------------------------
# 设计一个函数返回列表最大和第二大的元素的值
def max2(li):
    m1, m2 = (li[0], li[1]) if li[0] > li[1] else (li[1], li[0])
    for index in range(2, len(li)):
        if li[index] > m1:
            m2 = m1
            m1 = li[index]
        elif li[index] > m2:
            m2 = li[index]
    return m1, m2


# -----------------------------------------------------------------
# 计算制定的某天是这一年的第几天
def is_leap_yera(year):
    if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
        print("闰年")
        return True


def which_day(year, month, day):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_yera(year):
        month_days[1] = 29
    total = 0
    for index in range(month - 1):
        total += month_days[index]
    return total + day

# -----------------------------------------------------------------
# 打印杨辉三角
def san_jiao(rows):
    yh = [[]] * rows
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)

        for col in range(len(yh[row])):

            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

# -----------------------------------------------------------------
# 双色球选号
from random import randrange,randint,sample

def display(balls):
    for index,ball in enumerate(balls):
        if index == len(balls)-1:
            print("|",end=" ")
        print("%02d" %ball,end=" ")
    print()

def  select_ball():
    red_balls = [x for x in range(1,34)]
    blue_ball =random.randrange(1,17)
    balls = []
    for _ in range(6):
        index =randrange(len(red_balls))
        balls.append(red_balls[index])
        red_balls.pop(index)
    balls.sort()
    balls.append(blue_ball)
    return balls


# -----------------------------------------------------------------
# 约瑟夫环问题

def yuese():
    person = [True]*30
    counter,index,number =0,0,0
    while counter <15:
        if person[index]:
            number +=1
            if number == 9:
                person[index] = False
                counter += 1
                number = 0
        index += 1
        index %=30
    print(len(person))
    for  per in person:
        print (per,end = "")
        print("基" if per else "非基",end="" )


# -----------------------------------------------------------------
#井字棋游戏
import os
def print_board(board):
    print(board['TL']+'|'+board['TM']+'|'+board['TR'])
    print('-+-+-')
    print(board['ML']+'|'+board['MM']+'|'+board['MR'])
    print('-+-+-')
    print(board['BL']+'|'+board['BM']+'|'+board['BR'])

def jing_main():
    init_board ={
        'TL':' ', 'TM':' ', 'TR':' ',
        'BL':' ', 'BM':' ' ,'BR':' ',
        'ML': ' ', 'MM': ' ', 'MR': ' '
    }
    began = True
    while began:
        curr_board = init_board.copy()
        began = False
        turn = 'x'
        counter = 0
        os.system('clear')
        print_board(curr_board)
        while counter <9:
            move = input('轮到%s走棋,请输入位置'%turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move]=turn

                if turn == 'x':
                    turn='o'
                else :
                    turn ='x'
            os.system("clear")
            print_board(curr_board)
        choice = input("再玩一局?(yes/no)")
        began = choice =='yes'







if __name__ == "__main__":
    # guan_gao("北京欢迎你")
    # print(generate_code(4))
    # print(get_suffix("jaodi.txt", True))
    # print(max2([12, 34, 78, 45, 69]))
    # print(which_day(2000, 5, 5))
    # san_jiao(7)
    # display(select_ball())
    # yuese()
    jing_main()
