#2  折半查找（条件-排序好的列表）
def half_find(li,key):
    start = 0
    end = len(li)

    while start<=end:
        half = (start + end) // 2
        if key == li[half]:
            return half
        elif key> li[half]:
            start=half+1
        elif key < li[half]:
            end=half
    return -1
#泡沫排序
def bubble_sort(li):
    n = len(li)
    for i in range(n-1):
        for j in range(n-i-1):
            if li[j]> li[j+1]:
                li[j],li[j+1]= li[j+1],li[j]
    print(li)
#插入排序
def select_sort(li):
    n = len(li)
    for i in range(n):
        temp = li[i]
        for j in range(i + 1, n):
            if temp > li[j]:
                temp,li[j] =li[j],temp
        if li[i] !=temp:
            li[i] = temp
    print(li)
li = [1,4,5,7,3,2,112,6]
bubble_sort(li)



li = [1,4,5,7,3,2,112,6]
select_sort(li)
#插入排序
def insert(li):
    n = len(li)
    for index in range(1,len(li)):
        #从第二个位置开始插入
        tem = li[index]
        j = index-1
        while j >=0 and  tem < li[j]:
            li[j+1]=li[j]
            j -=1
        li[j+1] = tem

    print(li)

li = [1,4,5,7,3,2,112,6]
insert(li)

def shell_sort(li,increat):

    for inc in increat:
        for index in range(inc,len(li)):
            tem= li[index]
            j =index-inc
            while j >= 0  and tem< li[j]:
                li[j+inc]= li[j]
                j -= inc
            li[j+inc] = tem
    print(li)

li = [1,4,5,7,3,2,112,6,9,8]
shell_sort(li,[1])

#快速排序
def find_mid_point(li, left, right):

    mid_point = li[left]
    while left<right:

        while left<right and mid_point<li[right]:
            right -=1

        li[left] = li[right]
        while left<right and mid_point>li[left]:
            left +=1
        li[right] = li[left]

    return left


def quickly(li,left,right):
    if left <right:
        mid_point =  find_mid_point(li,left,right)
        quickly(li,left,mid_point-1)
        quickly(li,mid_point+1,right)



li = [1,4,5,7,3,2,112,6,9,8]
# quickly(li,0,len(li)-1)
# print(li)

def quick_sort(li,left,right):
    if left<right:
        mid_point = get_mid_point(li,left,right)
        quick_sort(li,left,mid_point-1)
        quick_sort(li,mid_point+1,right)

def get_mid_point(li,left,right):
    mid_point = li[left]
    while left < right:
        while left < right and mid_point < li[right]:
            right -=1
        li[left] = li[right]
        while left <right and li[left] <mid_point:
            left +=1
        li[right] = li[left]

    li[left] = mid_point
    return left

quick_sort(li,0,len(li)-1)
print(li)
#归并排序

def _merge_sort(li, low, mid, high):
    i = low
    j = mid+1
    result = []
    while i<= mid and j<= high:
        if li[i] <li[j]:
            result.append(li[i])
            i +=1
        else:
            result.append(li[j])
            j +=1

    while i<= mid:
        result.append(li[i])
        i +=1

    while j<=high:
        result.append(li[j])
        j +=1

    li[low: high + 1] = result



def merge(li,low,high):
    if low< high:
        mid = (low+high)//2

        merge(li,low,mid)
        merge(li,mid+1,high)

        _merge_sort (li,low,mid,high)


li = [1,4,5,7,3,2,112,6,9,8]
merge(li ,0,len(li)-1)
print(li)

