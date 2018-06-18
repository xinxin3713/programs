#!/usr/bin/env python
# _*_coding:utf-8 _*_

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/6/1"


import pandas as pd
import numpy as np
from sklearn.linear_model import  LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv('testSet.txt',sep='\t',header=None,names=['A','B','C'])
x = data.iloc[:,:-1]
x['D']=1.0
y = data['C']
# m,n = np.shape(x)
# alpha = 0.001
# max_cycles =500
# weights = pd.Series([1 for _ in range(n)],index=['D','A','B'])
#
# #
# for k in range(max_cycles):
#     temp = np.exp(x.mul(weights,axis =1).sum(axis=1))
#     temp =1/(1+temp)
#     error = y-temp
#     weights -=alpha*np.sum(x.transpose()*error,axis=1)
#
# print(weights)

model = LogisticRegression()
model.fit(x,y)
pred = model.predict(x)

print(accuracy_score(pred,y))




