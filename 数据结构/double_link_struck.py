#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/4/12"


class Node(object):
    '''
    双向链表节点
    '''

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DLinkList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def length(self):

        length = 0
        p = self.head
        while p != None:
            length += 1
            p = p.next
        return length

    def travel(self):

        p = self.head
        while p != None:
            print(p.item)
            p = p.next
        print('')

    def getitem(self, index):
        if self.is_empty() or index < 0 or index > self.length():
            print('link list is empty ')
            return

        p = self.head
        j = 0
        while p != None and j < index:
            j += 1
            p = p.next
        if j == index:
            print(p.item)
        else:
            print('not exist')

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node

        p = self.head
        while p.next != None:
            p = p.next

        p.next = node
        node.prev = p

    def search_rtn_index(self, item):
        p = self.head
        j = 0
        while p != None:
            if p.item ==item:
                return j
            p = p.next
            j +=1

        return -1

    def insert(self, index, item):

        if index <= 0:
            self.add(item)

        elif index > (self.length() - 1):
            self.append(item)

        else:
            node = Node(item)
            p = self.head
            j = 0
            # 移动到指定位置的前一个位置
            while j < index-1:
                p = p.next
                j += 1

            node.prev = p
            node.next = p.next
            p.next = node
            p.next.prev = node

    def remove(self, item):
        if self.is_empty():
            print('link list is empty')
            return

        else:
            p = self.head
            if p.item == item:
                if p.next == None:

                    self.head = None

                else:
                    p.next.prev = None
                    self.head = p.next
                return

            while p != None:
                if p.item == item:
                    p.prev.next = p.next
                    p.next.prev = p.prev
                p = p.next
if __name__ == "__main__":
    ll = DLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(8, 4)
    ll.insert(1, 5)
    ll.insert(0, 6)
    print ("length:",ll.length())
    ll.travel()
    ll.getitem(2)
    print (ll.search_rtn_index(3))
    print (ll.search_rtn_index(4))
    ll.remove(1)
    print( "length:",ll.length())
    ll.travel()