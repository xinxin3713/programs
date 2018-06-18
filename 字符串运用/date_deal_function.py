
def map(fun,iter):
    result = []
    for item in iter:
        result.append(fun(item))
    return result

def fiter (fun,iter):
    result = []
    for item in iter:
        if fun(item):
            result.append(item)
    return result

def reduce(fun,iter,init_arg):
    result = init_arg
    for item in iter:
        result=fun(result,item)
    return result


from  toolz.curried import map
from pylab import hist,show,xticks,title
