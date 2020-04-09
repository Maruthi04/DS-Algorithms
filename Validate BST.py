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
    def isValidBST(self, root):
        current = root  
        stack = [] # initialize stack 
        done = 0 
        arr=[]
        while True: 
            if current is not None: 
                stack.append(current) 
                current = current.left  

            elif(stack): 
                current = stack.pop() 
                print(current.val, end=" ")
                arr.append(current.val)
                current = current.right  

            else: 
                break
        for i in range(len(arr)-1):
            if(arr[i]>=arr[i+1]):
                return False
        return True
obj=Solution()
root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(5) 
root.right.left = Node(2) 
print(obj.isValidBST(root)) 