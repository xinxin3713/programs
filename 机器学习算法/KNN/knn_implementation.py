#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/5/9"

import csv
import  random
import math
import operator
import pandas as pd


#1,导入数据,分两部分,训练和测试
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])

#2,计算距离
def euclideanDistance(instance1, instance2, length):
    '''

    :param instance1: 一行数据 列表
    :param instance2: 一行数据 列表
    :param length:
    :return:
    '''
    distance = 0
    for x in range(length):
        distance += pow((instance1[x]-instance2[x]), 2)
    return math.sqrt(distance)
#3,获取距离最近的的K个元素,少数服从多数的原则决定它的类别
def getNeighbors(trainingSet, testInstance, k):
    '''

    :param training_set: 多维数据
    :param test_instance: 一维数据
    :param k:
    :return:
    '''
    distances = []
    length = len(testInstance) - 1

    train_len = len(trainingSet)
    print(length,train_len)
    for x in range(train_len):
        # testinstance
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    #根据序号1,dist大小来排序
    distances.sort(key=operator.itemgetter(1))
    neighbors =[]
    for x in range(k):
        neighbors.append(distances[x][0])
        return neighbors

#4,统计k里面类别数最多的一个

def get_response(neighbors):
    count_dict = {}
    for index in range(len(neighbors)):
        count_dict[index]= count_dict.get(index,0)+1


#5 预测,计算准确率
def get_accuracy(test_set,predictions):
    correct = 0
    for x in range(len(test_set)):

        if test_set[x][-1] == predictions[x]:
            correct += 1

    return (correct/float(len(test_set)))*100

if __name__ == '__main__':
    trainingSet=[]
    testSet=[]
    split = 0.67
    loadDataset('irisdata.txt', split, trainingSet, testSet)
    print ('Train set: ' + repr(len(trainingSet)),trainingSet)
    print ('Test set: ' + repr(len(testSet)),testSet)
    k = 3
    predictions = []
    for x in range(len(testSet)):
        neightbors = getNeighbors(trainingSet,testSet[x],k)
        result = get_response(neightbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = get_accuracy(testSet, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')