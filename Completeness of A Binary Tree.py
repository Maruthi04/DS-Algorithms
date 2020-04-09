# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Node:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Solution:
    def isCompleteTree(self, root):
        n=self.countNodes(root)
        return self.finder(root,0,n)
    def countNodes(self,root):
        if root is None:
            return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
    def finder(self,root,index,n):
        if root is None:
            return True
        if index>=n:
            return False
        return self.finder(root.left,2*index+1,n) and self.finder(root.right,2*index+2,n)

obj=Solution()
root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(5) 
root.right.left = Node(2) 
print(obj.isCompleteTree(root)) 