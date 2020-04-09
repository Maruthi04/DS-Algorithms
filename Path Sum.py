# Definition for a binary tree node.
class Node:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        path=[]
        return self.myfun(root,path,0,sum)
    def myfun(self,root,path,pathlength,sum1):
        if(root is None):
            return
        if(len(path)>pathlength):
            print(root.val,len(path),pathlength,path)
            path[pathlength]=root.val
            print(path)
        else:
            path.append(root.val)
            print(root.val,path,pathlength)
        pathlength+=1
        if(root.left is None and root.right is None):
            #print(path[:pathlength],sum(path[:pathlength]))
            return sum(path[:pathlength])==sum1
        else:
            #print("before recursion ",root.val,pathlength,sum1)
            return self.myfun(root.left,path,pathlength,sum1) or self.myfun(root.right,path,pathlength,sum1)
obj=Solution()
root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(5) 
root.right.left = Node(2) 
print(obj.hasPathSum(root,14)) 
