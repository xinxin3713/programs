#!/usr/bin/env python
# _*_coding:utf-8 _*_
from numpy.random import rand

__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/5/23"


# 1从文件加载数据集
def load_data(filename):
    data_mat = []
    f = open(filename, 'r')
    for line in f.readlines():
        line_list = line.strip().split()
        # print(line_list)
        # 迭代器
        flt_line = list(map(float, line_list))
        # 列表
        data_mat.append(flt_line)

    return data_mat


# print(load_data('testSet.txt'))

from numpy import mat, sqrt, shape, zeros, inf, nonzero, mean, power,sum


# print(data_mat)
def dist_eclud(vec_a, vec_b):
    '''
    计算两个向量的欧式距离
    :param vec_a:
    :param vec_b:
    :return:
    '''
    return sqrt(sum(power(vec_a - vec_b,2)))


def rand_cent(data, k):
    n = shape(data)[1]  # 列数
    centroids = mat(zeros((k, n)))  # 创建k个质心矩阵
    for j in range(n):
        min_j = min(data[:, j])
        range_j = float(max(data[:, j]) - min_j)
        centroids[:, j] = mat(min_j + range_j * rand(k,1))
    return centroids


def k_means(data, k, distMeas=dist_eclud, createCent=rand_cent):
    '''
     # 该算法会创建k个质心，然后将每个点分配到最近的质心，再重新计算质心。
    # 这个过程重复数次，直到数据点的簇分配结果不再改变位置。
    # 运行结果（多次运行结果可能会不一样，可以试试，原因为随机质心的影响，但总的结果是对的， 因为数据足够相似，也可能会陷入局部最小值）
    :param data:
    :param k:
    :param distMeas:
    :param createCent:
    :return:
    '''
    m = shape(data)[0]#行数
    # 创建一个与 data 行数一样，但是有两列的矩阵，用来保存簇分配结果
    cluster_assment = mat(zeros((m,2)))
    # 创建质心，随机k个质心
    centroids = createCent(data,k)
    cluster_changed = True
    while cluster_changed:
        cluster_changed=False
        # 循环每一个数据点并分配到最近的质心中去
        for i in range(m):
            min_dist =inf
            min_index = -1
            for j in range(k):
                # 计算数据点到质心的距离
                dist_ji=distMeas(centroids[j,:],data[i,:])
                # 如果距离比 minDist（最小距离）还小，更新 minDist（最小距离）和最小质心的 index（索引
                if dist_ji<min_dist:
                    min_dist =dist_ji
                    min_index = j
            if cluster_assment[i,0] != min_index: # 簇分配结果改变
                cluster_changed =True
                cluster_assment[i,:] = min_index,min_dist**2
        print(centroids)
        #更新质心
        for cent in range(k):
            pts_clust = data[nonzero(cluster_assment[:,0].A ==cent)[0]]
            centroids[cent,:]=mean(pts_clust,axis=0)
    return centroids,cluster_assment


def biKMeans(dataSet, k, distMeas=dist_eclud):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2))) # 保存每个数据点的簇分配结果和平方误差
    centroid0 = mean(dataSet, axis=0).tolist()[0] # 质心初始化为所有数据点的均值
    centList =[centroid0] # 初始化只有 1 个质心的 list
    for j in range(m): # 计算所有数据点到初始质心的距离平方误差
        clusterAssment[j,1] = distMeas(mat(centroid0), dataSet[j,:])**2
    while (len(centList) < k): # 当质心数量小于 k 时
        lowestSSE = inf
        for i in range(len(centList)): # 对每一个质心
            ptsInCurrCluster = dataSet[nonzero(clusterAssment[:,0].A==i)[0],:] # 获取当前簇 i 下的所有数据点
            centroidMat, splitClustAss = k_means(ptsInCurrCluster, 2, distMeas) # 将当前簇 i 进行二分 kMeans 处理
            sseSplit = sum(splitClustAss[:, 1])  # 将二分 kMeans 结果中的平方和的距离进行求和
            sseNotSplit = sum(
                clusterAssment[nonzero(clusterAssment[:, 0].A != i)[0], 1])  # 将未参与二分 kMeans 分配结果中的平方和的距离进行求和
            print("sseSplit, and notSplit: ", sseSplit, sseNotSplit)

            if (sseSplit + sseNotSplit) < lowestSSE:  # 总的（未拆分和已拆分）误差和越小，越相似，效果越优化，划分的结果更好（注意：这里的理解很重要，不明白的地方可以和我们一起讨论）
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
            # 找出最好的簇分配结果
        bestClustAss[nonzero(bestClustAss[:, 0].A == 1)[0], 0] = len(centList)  # 调用二分 kMeans 的结果，默认簇是 0,1. 当然也可以改成其它的数字
        bestClustAss[nonzero(bestClustAss[:, 0].A == 0)[0], 0] = bestCentToSplit  # 更新为最佳质心
        print('the bestCentToSplit is: ', bestCentToSplit)
        print('the len of bestClustAss is: ', len(bestClustAss))

        # 更新质心列表
        centList[bestCentToSplit] = bestNewCents[0, :].tolist()[0]  # 更新原质心 list 中的第 i 个质心为使用二分 kMeans 后 bestNewCents 的第一个质心
        centList.append(bestNewCents[1, :].tolist()[0])  # 添加 bestNewCents 的第二个质心
        clusterAssment[nonzero(clusterAssment[:, 0].A == bestCentToSplit)[0], :] = bestClustAss  # 重新分配最好簇下的数据（质心）以及SSE
    return mat(centList), clusterAssment

if __name__ == '__main__':
    # 1生成需要的数据格式
    data_mat = mat(load_data('testSet.txt'))
    print(len(data_mat))
    myCentroids, clustAssing = biKMeans(data_mat, 4)
    print("=============================================")
    print(myCentroids)
    print("=============================================")
    print(clustAssing,len(clustAssing))
