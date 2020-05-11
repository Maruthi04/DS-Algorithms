class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def insert(root,node):
    q=[]
    q.append(root)
    while q:
        root=q.pop(0)
        if root.left is None:
            root.left=node
            break
        else:
            q.append(root.left)
        if root.right is None:
            root.right=node
            break
        else:
            q.append(root.right)
def deletedeep(root,node):
    q=[]
    q.append(root)
    while q:
        root=q.pop(0)
        if root==node:
            root=None
            break
        if root.left is not None:
            if root.left==node:
                root.left=None
                break
            else:
                q.append(root.left)
        if root.right is not None:
            if root.right ==node:
                root.right=None
                break
            else:    
                q.append(root.right)
        
def delete(root,key):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.val==key:
            return None
        else:
            return root
    q=[]
    q.append(root)
    key_node=None
    while q:
        node=q.pop(0)
        if node.val==key:
            key_node=node
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    if key_node:
        x=node.val
        print("the last node is ",node.val)
        deletedeep(root,node)
        key_node.val=x
                
                
def levelorder(root):
    stack=[]
    stack.append(root)
    while stack:
        node=stack.pop(0)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
        print(node.val)
root=Node(40)
insert(root,Node(50))
insert(root,Node(60))
levelorder(root)
delete(root,50)
levelorder(root)