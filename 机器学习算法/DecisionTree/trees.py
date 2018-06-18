#!/usr/bin/env python
# _*_coding:utf-8 _*_

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/2/2"

from math import log

def calcShannonEnt(dataSet):
    '''
    计算信息熵
    :param dataSet:
    :return:
    '''
    num_entries = len(dataSet)
    label_counts ={}

    for feat in dataSet:
        current_label = feat[-1]
        if current_label not in label_counts.keys():
            label_counts[current_label]=0
        label_counts[current_label] +=1
    
    shannon_ent = 0.0
    for key in label_counts:
        prob = float(label_counts[key])/num_entries
        shannon_ent -=prob*log(prob,2)
    return shannon_ent