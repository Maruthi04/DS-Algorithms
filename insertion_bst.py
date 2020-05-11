def insert(root,val):
    if root is None:
        root=Node(val)
    elif val <root.val and root.left is None:
        root.left=Node(val)
    elif val>root.right and root.right is None:
        root.right=Node(val)
    elif val<root.val and root.left is not None:
        insert(root.left,val)
    elif val>root.val and root.right is not None:
        insert(root.right,val)
class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
t = int(input())

arr = list(map(int, input().split()))
root=Node(arr[0])
for i in range(1,t):
    insert(root,arr[i])
preorder(root)