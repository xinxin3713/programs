from numpy import *
import operator
def  creat_data_set():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels
group,labels = creat_data_set()
print(group,labels)

def classify(inX,dataSet,labels,k):
    '''
    knn求距离最近的k个数据的labels,
    按哪个比例多的原则划分
    :param inX: 坐标数据
    :param dataSet: 矩阵数据
    :param labels: 标记值
    :param k: 参数k
    :return:
    '''
    #获取行数
    dataSetSize = dataSet.shape[0]
    #把坐标转化成训练矩阵相同的shape,每行都是坐标的数据
    #在两个矩阵相减
    diffMat = tile(inX,(dataSetSize,1))-dataSet
    #平方,
    sqDiffMat = diffMat**2
    #每行求和
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    print('distances',distances)

    # distances [0.78102497 0.70710678 0.70710678 0.64031242]
    sortedDistIndicies  = distances.argsort()
    print('sortedDistIndicies',sortedDistIndicies)
    # sortedDistIndicies对距离原地排序 [3 1 2 0]
    classcount ={}
    for i in range(k):#K的取值为labels长度少一
        votelabel = labels[sortedDistIndicies[i]]#通过排序后的序号获取对应的labels分类
        classcount[votelabel] = classcount.get(votelabel,0)+1#有分类key 的value进行加一操作，
    print(classcount)
    #{'B': 2, 'A': 1}
    #字典根据value来排序
    sortedclasscount = sorted(classcount.items(),key = operator.itemgetter(1),reverse=True)
    print(sortedclasscount)
    #[('B', 2), ('A', 1)]
    return sortedclasscount[0][0]

print(classify([0.5,0.5],group,labels,3))



