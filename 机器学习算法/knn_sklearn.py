#!/usr/bin/env python
# _*_coding:utf-8 _*_

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/5/20"


from sklearn import neighbors
from sklearn import datasets

knn_modle = neighbors.KNeighborsClassifier()

iris = datasets.load_iris()


knn_modle.fit(iris.data,iris.target)

pre_result = knn_modle.predict([[7.1, 3.2, 2.3, 3.4]])
print(pre_result)
