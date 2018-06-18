from numpy import *
def file2matrix(filename):
    fr = open(filename)
    arrayOlines = fr.readlines()
    numOfLines=len(arrayOlines)
    returnMat = zeros((numOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOlines:
        line = line.strip()
        listFromLine = line.split('\t')
        #print(listFromLine)
        returnMat[index,:]= listFromLine[0:3]
        #print(returnMat)
        classLabelVector.append((listFromLine[-1]))
        index +=1
    return returnMat,classLabelVector
datingDataMat, datingLabels=(file2matrix("datingTestSet2.txt"))
#print(datingDataMat[:,1])
def autoNorm(dataset):
    min_vals = dataset.min(0)
    max_vals = dataset.max(0)
    ranges = max_vals - min_vals
    norm_data_set = zeros(shape(dataset))
    m = dataset.shape[0]
    norm_data_set = dataset - tile(min_vals,(m,1))
    norm_data_set = norm_data_set / tile(ranges,(m,1))
    return  norm_data_set,ranges,min_vals
norm_mat,ranges,min_vals =autoNorm(datingDataMat)
print(norm_mat)
print(ranges,min_vals)
import  matplotlib.pyplot as plt
import pylab as pl
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
plt.show()