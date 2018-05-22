#!/usr/bin/env python
# _*_coding:utf-8 _*_

from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/5/18"


#read in the csv file
all_electronics =open('AllElectronics.csv','rt')
reader = csv.reader(all_electronics)
head = reader.__next__()
print(head)
#put feature in a list of dict
# 把数据转化成训练集的模式
feature_list =[]
label_list = []
for row in reader:
    label_list.append((row[-1]))
    row_dict ={}
    for i  in range(1,len(row)-1):
        row_dict [head[i]]=row[i]

    feature_list.append(row_dict)
print(feature_list)
print(label_list)

#然后转化成数字特征集 比如age有三个类别 001,010,100用三个数字位表示
vec = DictVectorizer()
dummyX = vec.fit_transform(feature_list) .toarray()

print("dummyX: " + str(dummyX))
print(vec.get_feature_names())
lab = preprocessing.LabelBinarizer()
dummyY = lab.fit_transform(label_list)
# le  = preprocessing.LabelEncoder()
# le.fit_transform() #变换成0-n 某列分成n中类别
print("dummyY: " + str(dummyY))


#准备训练,调用训练模型
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX,dummyY)
print("ctf: " + str(clf))

# Visualize model
with open("allElectronicInformationGainOri.dot", 'w') as f:
    f= tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=f)

oneRowX = dummyX[0, :]
print("oneRowX: " + str(oneRowX))

newRowX = oneRowX
newRowX[0] = 1
newRowX[2] = 0
print("newRowX: " + str(newRowX))

predictedY = clf.predict(newRowX)
print("predictedY: " + str(predictedY))