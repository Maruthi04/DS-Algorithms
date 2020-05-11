# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 03:44:03 2020

@author: tinku
"""

class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
def preorder(root):
    stack=[]
    stack.append(root)
    while stack:
        node=stack.pop(0)
        print(node.val)
        if node.right:
            stack.append(node.left)
        if node.left:
            stack.append(node.right)
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.left=Node(60)
root.right.right=Node(70)
preorder(root)            
