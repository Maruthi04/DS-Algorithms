# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 04:10:08 2020

@author: tinku
"""

class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
def peek(stack):
    if len(stack)>0:
        return stack[-1]
def postorder(root):
    stack=[]
    while True:
        while root:
            if root.right is not None:
                stack.append(root.right)
            stack.append(root)
            root=root.left
        root=stack.pop()
        if root.right is not None and peek(stack)==root.right:
            stack.pop()
            stack.append(root)
            root=root.right
        else:
            print(root.val)
            root=None
        if len(stack)<=0:
            break
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.left=Node(60)
root.right.right=Node(70)
postorder(root)            

            