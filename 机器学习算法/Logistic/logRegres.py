import math
import numpy
def load_data_set():
    data_mat = []
    label_mat = []
    fr = open('testSet.txt')
    for line in fr:
        line_arr = line.strip().split()
        data_mat.append([1.0,float(line_arr[0]),float(line_arr[1])])
        label_mat.append(int(line_arr[2]))
    return data_mat,label_mat

def sigmoid(inx):
    return 1.0/(1+numpy.exp(inx))

def grad_ascent(data_mat_in,class_labels):
    data_matrix = numpy.mat(data_mat_in)
    label_mat = numpy.mat(class_labels).transpose()

    m,n = numpy.shape(data_matrix)
    alpha = 0.001
    max_cycles = 500
    weights = numpy.ones((n,1))

    # h = sigmoid(data_matrix * weights)
    # print(h)
    # error = (label_mat - h)
    # print(error)
    # weights = weights - alpha * data_matrix.transpose() * error

    for k in range(max_cycles):
        h = sigmoid(data_matrix*weights)
        error = (label_mat -h)
        weights = weights - alpha*data_matrix.transpose()*error
    return  weights
def plot_best_fit(weights):
    import array
    import random
    import  matplotlib.pylab as plt
    data_mat,label_mat = load_data_set()
    data_arr = numpy.array(data_mat)
    n = numpy.shape(data_arr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if int(label_mat[i])==1:
            xcord1.append(data_arr[i,1])
            ycord1.append(data_arr[i,2])
        else:
            xcord2.append(data_arr[i,1])
            ycord2.append(data_arr[i,2])
    fig  =  plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1,ycord1,s=30,c='red',marker='s')
    ax.scatter(xcord2,ycord2, s=30, c='green')
    x =numpy.arange(-3.0,3.0,0.1)
    y  = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x,y)
    plt.xlabel("X1")
    plt.ylabel(("X2"))
    plt.show()





if __name__=='__main__':
    data_arr,label_mat = load_data_set()
    print('data_arr',data_arr,)
    print('label_mat',label_mat)
    weights = grad_ascent(data_arr,label_mat)
    print('weights',weights)
    plot_best_fit(weights.getA())