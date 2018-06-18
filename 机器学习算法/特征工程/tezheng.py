#!/usr/bin/env python
# _*_coding:utf-8 _*_

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/6/3"
import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer

iris = load_iris()
data=iris.data
max_data = data.max(axis =0)
min_data = data.min(axis =0)
tem_data = max_data-min_data
top_data =data-min_data
guiyi_data =top_data/tem_data
print('归一化',guiyi_data[0,])
data_minmax = MinMaxScaler().fit_transform(iris.data)
print('归一化',data_minmax[0,])
data_nor =  Normalizer().fit_transform(iris.data)
print('Normalizer归一化',data_nor[0,])
#############################################################

x = data.mean(axis = 0)
print('mean',x)
data_mean = data-x
data_var = data.std(axis=0)
#print('标准方差',data_var)
data =data_mean/data_var
print('标准化数据',data[0,])
data = StandardScaler().fit_transform(iris.data)
print('标准化数据',data[0,])
print('原始数据',iris.data[0,])
###############################################################

from sklearn.preprocessing import Binarizer
data = Binarizer(threshold=3).fit_transform(iris.data)
print('Bindarizer二值化',data[0,])

####################################################################

from sklearn.preprocessing import OneHotEncoder
target = OneHotEncoder().fit_transform(iris.target.reshape((-1,1)))
print('target哑编码',target)

################################################################

from sklearn.preprocessing import  Imputer
data_impu = Imputer().fit_transform(np.vstack((np.array([np.nan,np.nan,np.nan,np.nan]),iris.data)))
print('data_impu',data_impu[0,])

###################################################################3

from sklearn.preprocessing import PolynomialFeatures
data_poly = PolynomialFeatures().fit_transform(iris.data)
print('data_poly',data_poly[0,])
# iris.data
#
# iris.target

