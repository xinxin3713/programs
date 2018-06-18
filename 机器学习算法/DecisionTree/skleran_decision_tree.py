#!/usr/bin/env python
# _*_coding:utf-8 _*_

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/6/3"

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder,LabelBinarizer

data =pd.read_csv('AllElectronics.csv')
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
#print(x.columns)

#1先将字符转化成数字
for col in x.columns:
    if isinstance(x[col][0],str):
        x[col] = LabelBinarizer().fit_transform(x[col])
y = LabelBinarizer().fit_transform(y)
print(x)
#print(y)


