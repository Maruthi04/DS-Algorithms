class Node(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def insert(root,key):
    if(root is None):
        root=key
    else:
        if(key.val<root.val):
            if(root.left is not None):
                insert(root.left,key)
            else:
                root.left=key
        elif(key.val>=root.val):
            if(root.right is not None):
                insert(root.right,key)
            else:
                root.right=key
def delete(root,key):
    if(root is None):
        return root
    else:
        if(key<root.val):
            root.left=delete(root.left,key)
        elif(key>root.val):
            root.right=delete(root.right,key)
        else:
            if(root.left is None):
                temp=root.right
                root=None
                return temp
            elif(root.right is None):
                temp=root.left
                root=None
                return temp
            else:
                temp=getMinimum(root.right)
                root.val=temp.val
                root.right=delete(root.right,temp.val)
        return root
def search(root,key):
    if(root is None):
        return root
    else:
        if(key<root.val):
            return search(root.left,key)
        elif(key>root.val):
            return search(root.right,key)
        else:
            return root.val
            
def getMinimum(root):
    if root is None or root.left is None:
        return root
    else:
        return getMinimum(root.left)
    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        

root=Node(10)
insert(root,Node(40))
insert(root,Node(20))
insert(root,Node(30))
insert(root,Node(50))
insert(root,Node(70))
insert(root,Node(90))
delete(root,30)
delete(root,50)
delete(root,90)

inorder(root)
print("the element is ",search(root,20))

    