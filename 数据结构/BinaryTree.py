#!/usr/bin/env python
# _*_coding:utf-8 _*_
__title__ = ''
__author__ = "liuxin"
__mtime__ = "2018/4/13"

class TreeNode(object):
    def __init__(self,key,left=None,right=None,parent=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_right_child(self):
        return self.parent and self.parent.right ==self

    def is_left_child(self):
        return self.parent and self.parent.left ==self





class BSTree (object):
    def __init__(self):
        self.root =None
        self.size = 0

    def length(self):
        return self.size

    def insert(self,item):
        node = TreeNode(item)
        if not self.root:
            self.root = node
            self.size +=1

        else:
            current_node = self.root
            while True:
                if item <current_node.key:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = node
                        node.parent = current_node
                        self.size +=1
                        break
                elif item > current_node.key:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = node
                        node.parent = current_node
                        self.size +=1
                        break

                else:
                    break

    def find(self,key):

        if self.root:
            res = self._find(key,self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def _find(self,key,node):
        if not node:
            return None
        elif node.key ==key:
            return node
        elif key < node.key:
            return self._find(key,node.left)
        else:
            return self._find(key,node.right)

    def find_min(self):

        if self.root:
            current = self.root
            while current.left:
                current = current.left

            return current
        else:
            return None

    def _find_min(self,node):
        if node:
            current = node
            while current.left:
                current = current.left
            return current

    def find_max(self):

        if self.root:
            current = self.root
            while current.right:
                current = current.right

            return current

        else:
            return  None
    def delete(self,key):

        if self.size >1:
            node_del = self.find(key)
            if node_del:
                self.remove(node_del)
                self.size -=1
            else:
                raise KeyError("Error,key not in tree")

    def remove(self,node):
        if not node.left and not node.ring:
            if node == node.partent.left:
                node.parent.left = None
            else:
                node.parent.right = None

        elif node.left and node.right:
            min_node = self._find_min(node.right)
            node.key = min_node.key
            self.remove(min_node)

        else:
            if node.has_left_child():
                if node.is_left_chile():
                    node.parent.left= node.left
                elif node.is_right_child():
                    node.left.parent = node.parent
                    node.parent.right= node.left
                else:
                    self.root = node.right
                    node.right.parent=None
                    node.right = None 









