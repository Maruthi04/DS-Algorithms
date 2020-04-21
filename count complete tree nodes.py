# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if(root.left is not None and root.right is not None):
            #print(root.left.val,root.right.val,self.countNodes(root.left),self.countNodes(root.right))
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        if(root.left is not None and ro ot.right is None):
            #print(root.left.val,self.countNodes(root.left))
            return 1+self.countNodes(root.left)
        else:
            return 1
        