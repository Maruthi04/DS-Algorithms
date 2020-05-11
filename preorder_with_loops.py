class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
def preorder(root):
    if root is None:
        print("bcz of me")
        return 
    stack=[]
    stack.append(root)
    while stack:
        root=stack.pop()
        print(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
        
    
root=Node(10)
root.left=Node(20)
root.right=Node(30)
preorder(root)