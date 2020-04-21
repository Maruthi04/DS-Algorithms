# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp=None
        head1=head
        one=head
        two=head
        i=1
        if(head.next is None):
            return
        if self.lengthll(head)<=2 :
            if n==2:
                return head.next
            if n==1:
                head.next=None
                return head
                
        while True:
            if i<n:
                two=two.next
            if(i>=n):
                break
            i+=1
        while two.next:
            one=one.next
            two=two.next
        index=one
        print(index.val)
        nextval=index.next
        flag=0
        if head==index:
            return head.next
        while(head):
            
            if(head.next==index):
                head.next=nextval
                break
            head=head.next
        return head1
    def lengthll(self,root):
        count=0
        while(root):
            root=root.next
            count+=1
        return count
            
            
            
        