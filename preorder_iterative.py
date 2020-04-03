class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def iterativePreorder(root):
    stack=[]
    if(root is None):
        print("Go")
    else:  
        stack.append(root)
        while(len(stack)>0):
            node=stack.pop()
            print(node.data)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
    
root = Node(10) 
root.left = Node(8) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(5) 
root.right.left = Node(2) 
iterativePreorder(root) 
