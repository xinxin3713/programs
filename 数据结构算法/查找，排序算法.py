#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""

__created__ = '2017/1/10'
__author__ = 'liuxin'
"""
#顺序查找
def search(li , key ):
    for index, item in enumerate(li):
        if item == key:
            return index
    return -1

#2  折半查找（条件-排序好的列表）
def half_search(li , key ):
    start = 0
    end  = len(li)-1
    while start<=end:
        mid = (start+end)//2
        if  key == li[mid]:
            return mid
        elif key > li[mid]:
            start =mid +1
        elif key < li[mid]:
            end = mid -1
    return -1

#排序------------------------------------------
# 排序的程序

# 冒泡排序。
# 进行n - 1的操作，每一轮筛选出一个最大（小）的元素，放在列表的最后。
# 每一轮，每个元素与后面的元素进行比较，如果前面的比后面的大，则交换两个元素的位置。
def bubble(li):
    n = len(li)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]

li = [3, -2, 5, 10, -9, 11, 7, -1]
# bubble(li)
# print(li)

# 选择排序
# 进行n - 1轮的操作。通过变量保存最小元素的索引。（假定最开始的元素就是最小的元素。）然后与
# 后续的每个元素进行比较，如果发现更小的元素，则保存最小元素索引的变量更新。一轮过后，将
# 初始元素索引与变量保存的最小索引对应的元素进行交换。
def select(li):
    n = len(li)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if li[min_index] > li[j]:
                min_index = j
        if min_index != i:
            li[min_index], li[i] = li[i], li[min_index]

select(li)
print(li)

# 插入排序
# 从第2个元素开始（索引为1的元素），因此与其之前的元素进行比较，如果要插入的元素小于列表中现有的元素，
# 则现有的元素向后移动，在合适的位置，我们插入新的元素。
def insert(li):
    n = len(li)
    for i in range(1, n):
        temp = li[i]
        j = i - 1
        while j >= 0 and temp < li[j]:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp

insert(li)
print(li)

# 希尔排序
# 因为插入排序在元素有序的情况下，时间复杂度可以从O(n^2)提升到O(n)。希尔排序就是针对此情况，对插入排序进行的
# 一种改进。通过逐渐减少增量来使序列基本有序，从而可以提高插入排序的性能。希尔排序也称减少增量排序。
def shell(li, increment):
    n = len(li)
    for inc in increment:
        for i in range(inc, n):
            temp = li[i]
            j = i - inc
            while j >= 0 and temp < li[j]:
                li[j + inc] = li[j]
                j -= inc
            li[j + inc] = temp

shell(li, [5, 3, 1])
print(li)

# 快速排序：找到一个中心点（支点或枢轴），使得中心点右边的元素都大于中心点元素，而中心点左边的元素，都小于中心点元素。
# 然后这对中心点分隔的两个区间，递归的执行以上过程。
def quick(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick(li, left, mid - 1)
        quick(li, mid + 1, right)


def partition(li, left, right):
    pivot = li[left]
    while left < right:
        while left < right and pivot < li[right]:
            right -= 1
        li[left] = li[right]
        while left < right and pivot > li[left]:
            left += 1
        li[right] = li[left]
    li[left] = pivot
    return left

quick(li, 0, len(li) - 1)
print(li)

# 归并排序

# 将两个有序的序列合并成一个有序的序列。
# 先拆，拆到只剩下一个元素。（一个元素总是有序的），然后，再将各个有序的数据集合并。
# 最终合并成一个数据集。
li = [3, -2, 5, 10, -9, 11, 7, -1]

def merge(li, low, high):
    if low < high:
        mid = (low + high) // 2
        # [low,mid]    [mid + 1,high]
        merge(li, low, mid)
        merge(li, mid + 1, high)
        _merge_sort(li, low, mid, high)

# 合并的方法，将两个有序的数据集，合并成一个有序的数据集
def _merge_sort(li, low, mid, high):
    i = low
    j = mid + 1
    temp = []
    while i <= mid and j <= high:
        if li[i] <= li[j]:
            temp.append(li[i])
            i += 1
        else:
            temp.append(li[j])
            j += 1
    while i <= mid:
        temp.append(li[i])
        i += 1
    while j <= high:
        temp.append(li[j])
        j += 1
    li[low: high + 1] = temp

merge(li, 0, len(li) - 1)
print(li)