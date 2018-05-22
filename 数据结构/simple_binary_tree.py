#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/4/14"

import datetime


class Node(object):
    def __init__(self,data):
        self.item = data
        self.leftchild =None
        self.rightchild = None


class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.items = []

    def _empty(self):
        if self.root is None :
            return True
        else:
            return False


    def add(self,data):
        node = Node(data)
        if self.root is None :
            self.root = node
            self.items.append(self.root.item.item)
        else:
            root_node  = self.root
            while True:

                if node.item.item < root_node.item.item:
                    #move to left
                    if root_node.leftchild == None:
                        root_node.leftchild = node

                        break
                    else:
                        root_node = root_node.leftchild
                        self.items.append(root_node.item.item)


                elif node.item.item > root_node.item.item:
                    #move to right
                    if root_node.rightchild == None:
                        root_node.rightchild=node
                        break
                    else:
                        root_node = root_node.rightchild
                        self.items.append(root_node.item.item)

    def preorder(self,root,result = None):
        # if root is None:
        #     return []
        # result = [root.item.item]
        # left_item = self.preorder(root.leftchild)
        # right_item = self.preorder(root.rightchild)
        # return result + left_item + right_item
        if result is None :
            result=[]
        if root:

            result.extend([root.item.item])
            if root.leftchild:
                self.preorder(root.leftchild,result)

            if root.rightchild:
                self.preorder(root.rightchild,result)

        return result

    def inorder(self,root,result=None):
        if result is None :
            result=[]
        if root:
            if root.leftchild:
                self.inorder(root.leftchild,result)

            result.append(root.item.item)

            if root.rightchild:
                self.inorder(root.rightchild,result)
        return result

    def postorder(self,root,result=None):
        if result is None :
            result=[]
        if root:
            if root.leftchild:
                self.postorder(root.leftchild,result)

            if root.rightchild:
                self.postorder(root.rightchild,result)


            result.append(root.item.item)
        return result

if __name__ == '__main__':
    tree = BinaryTree()
    node1 = Node(10)
    node2 = Node(5)
    node3 = Node(7)
    node4 = Node(11)
    node5 = Node(15)
    node6 = Node(20)
    node7 = Node(12)

    for node in [node1,node2,node3,node4,node5,node6,node7]:
        tree.add(node)

    print(tree.preorder(tree.root))
    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))
    print(tree.postorder(tree.root))
#[7, 5, 12, 20, 15, 11, 10]



                