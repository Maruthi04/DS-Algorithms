class Treenode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.height=1
class AVL_tree(object):
    def insert(self,root,key):
        if not root:
            return Treenode(key)
        elif(key<root.val):
            root.left= self.insert(root.left,key)
        else:
            root.right= self.insert(root.right,key)
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
        balance=self.getBalance(root)
        if(balance<-1 and key>root.right.val):
            return self.leftRotate(root)
        if(balance>1 and key<root.left.val):
            return self.rightRotate(root)
        if(balance>1 and key>root.left.val):
            root.left=self.leftRotate(root.left)
            return self.rightRotate(root)
        if(balance<-1 and key<root.right.val):
            root.right=self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    def delete(self,root,key):
        if not root:
            return root
        elif key<root.val:
            root.left=self.delete(root.left,key)
        elif key>root.val:
            root.right=self.delete(root.right,key)
        else:
            if root.left is None:
                temp=root.right
                root=None
                return temp
            elif root.right is None:
                temp=root.left
                root=None
                return temp
            temp=self.getminimumNode(root.right)
            root.val=temp.val
            root.right=self.delete(root.right,temp.val)
        if root is None:
            return root
        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
        balance=self.getBalance(root)
        if(balance >1 and key<root.left.val):
            self.rightRotate(root)
        if(balance >1 and key>root.left.val):
            root.left=self.leftRotate(root.right)
            return self.rightrotate(root)
        if(balance <-1 and key>root.right.val):
            return self.leftrotate(root.val)
        if(balance<-1 and key<root.right.val):
            root.right=self.rightRotate(root.right)
            return self.leftrotate(root)
        return root
                
    def getminimumNode(self,root):
        if root is None or root.left is None:
            return root
        else:
            return self.getminimumNode(root.left)
    def getHeight(self,root):
        if(root==None):
            return 0
        return root.height
    def getBalance(self,root):
        if(root==None):
            return 0
        return self.getHeight(root.left)-self.getHeight(root.right)
    def rightRotate(self,z):
        y=z.left
        t2=y.right
        y.right=z
        z.left=t2
        z.height=1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    def leftRotate(self,z):
        y=z.right
        t3=y.left
        y.left=z
        z.right=t3
        z.height=1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    def preOrder(self,root):
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 
mytree=AVL_tree()
root=None
root=mytree.insert(root,10)
root=mytree.insert(root,20)
root=mytree.insert(root,30)
root=mytree.insert(root,40)
root=mytree.insert(root,50)
root=mytree.insert(root,25)
mytree.delete(root,20)
mytree.delete(root,10)
mytree.delete(root,30)

mytree.preOrder(root)


        
        