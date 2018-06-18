from __future__ import print_function

from time import time
import logging
import  matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn import  svm
from sklearn.metrics import accuracy_score
import pandas as pd

data  =  pd.read_csv('../irisdata.txt')

x = data.iloc[:,:-1]
y = data.iloc[:,-1]
train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.3)

# model = svm.SVC(C=10,kernel='rbf',gamma=1,decision_function_shape='ovo')
model = svm.SVC(C=3, kernel='poly', degree=3)
model.fit(train_x,train_y)
pred = model.predict(train_x)
print(accuracy_score(pred ,train_y))

test_pred = model.predict(test_x)
print(accuracy_score(test_pred,test_y))

