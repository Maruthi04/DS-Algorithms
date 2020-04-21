# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        arr=[]
        temp=head
        while head:
            arr.append(head.val)
            head=head.next
        arr1=[]
        for i in range(len(arr)):
            print(arr[(i+(len(arr)-k))%len(arr)])
            arr1.append(arr[(i+(len(arr)-k))%len(arr)])
        k=0
        final=temp
        while temp:
            temp.val=arr1[k]
            k+=1
            temp=temp.next
        return final
        
        