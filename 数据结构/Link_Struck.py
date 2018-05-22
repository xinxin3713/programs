#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/4/12"


class Node(object):
    '''
    定义一个链表的节点类
    包含 数据和下一个节点对象
    '''
    def __init__(self, val, p=None):
        self.data = val
        self.next = p


class LinkList(object):
    '''
    链表类
    '''
    def __init__(self):
        '''
        初始化类,头节点为0
        '''
        self.head = None

    def __getitem__(self, key):
        '''
        重写__getitem__方法
        增加了判断调用getitem时候自动执行
        :param key:
        :return:
        '''
        if self.is_empty():
            print('linklist is empty')
            return

        elif key < 0 or key > self.getlength():

            print('the given key is error')
            return

        else:
            return self.getitem(key)

    def initlist(self, data):
        '''
        初始化列表数据
        :param data: 数组
        :return:
        '''
        self.head = Node(data[0])
        p = self.head

        for i in data[1:]:
            #获取数据的第i个数据
            node = Node(i)
            #传到p.next
            p.next = node
            #把指针指到下一个数据
            p = p.next

    def getlength(self):
        '''
        获取链表的长度
        :return:
        '''
        p = self.head
        length = 0
        while p != None:
            length += 1
            p = p.next
        return length

    def is_empty(self):
        '''
        判断链表是否为空
        根据长度来判断
        :return:
        '''
        if self.getlength() == 0:
            return True
        else:
            return False

    def clear(self):
        '''
        清空数据
        :return:
        '''
        self.head = 0

    def append(self, item):
        '''
        表尾追加元素
        :param item:
        :return:
        '''
        #因为是最后一个,不用指定它的下一个元素
        q = Node(item)
        #判断位置是不是第一,代码严谨
        if self.head == 0:
            self.head = q
        else:
            p = self.head
            while p.next != 0:
                p = p.next
            p.next = q

    def getitem(self, index):
        '''
        通过索引获取值(data)
        :param index: 索引
        :return: data值
        '''
        if self.is_empty():
            print('Linklist is empty ')
            return

        j = 0
        p = self.head
        while p.next != 0 and j < index:
            p = p.next
            j += 1

        if j == index:
            return p.data
        else:
            print('not exist')

    def insert(self, index, item):
        '''
        插入数据:需要两个变量来保存插入的位置
        因为一个的话,.next后就发生变化了

        :param index: 插入位置
        :param item: 插入元素
        :return: null
        '''
        #判断是否为空,输入的index是否正确
        if self.is_empty() or index < 0 or index > self.getlength():
            print('link is empty')
            return

        #判断下是不是头位置插入
        if index == 0:
            q = Node(item, self.head)
            self.head = q

        j = 0
        p = self.head
        post = self.head

        while p != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if j == index:
            q = Node(item, p)
            post.next = q
            q.next = p.next

    def delete(self, index):

        if self.is_empty() or index < 0 or index > self.getlength():
            print('link list is empty')
            return

        if index == 0:
            q = Node(self.getitem(1), self.head)
            self.head = q

        p = self.head
        post = self.head
        j = 0
        while p != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if j == index:
            post.next = p.next

    def index(self, value):

        if self.is_empty():
            print('link list is empty')
            return

        p = self.head
        j = 0
        while p != 0 and not p.data == value:
            p = p.next
            j += 1
        if p.data == value:
            return j
        else:
            return -1

    def travel(self):
        '''
        遍历链表所有元素
        :return:
        '''
        if self.is_empty():
            print('link is empty')

        p = self.head
        while p !=None:
            print(p.data)
            p = p.next

if __name__ == "__main__":
    l = LinkList()
    l.initlist([1,2,3,4,5])
    l.travel()

    # print(l.getitem(4))
    # l.append(6)
    # print(l.getitem(5))
    # l.insert(3,9)
    # print(l.getitem(4))
    # l.delete(0)
    # print(l.getitem(0))
    # print(l.index(9))
    # print(l.getitem(3))

