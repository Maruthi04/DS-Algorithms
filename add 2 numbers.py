# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        temp1=l1
        temp2=l2
        fin1=l1
        arr=[]
        carry=0
        while temp1 and temp2:
            x=temp1.val+temp2.val+carry
            carry=0
            if x>9:
                carry=x//10
                x=x%10
                #print(carry,x,x//10)
            #print(x)
            arr.append(x)
            temp1=temp1.next
            temp2=temp2.next
        #print(temp1.val)
        while temp1 is not None:
            x=temp1.val+carry
            carry=0
            if(x>9):
                carry=x//10
                x=x%10
            arr.append(x)
            temp1=temp1.next
        while temp2 is not None:
            x=temp2.val+carry
            carry=0
            if(x>9):
                carry=x//10
                x=x%10
            arr.append(x)
            temp2=temp2.next
        print(carry)
        if(carry>0):
            arr.append(carry)
        while l1.next:
            l1=l1.next
        l1.next=l2
        count=0
        i=0
        ret=fin1
        while(i<len(arr)):
            fin1.val=arr[i]
            #print(fin1.val)
            i+=1
            prev=fin1
            fin1=fin1.next
        if fin1 is None:
            print("hii")
        xx=0
        hello=ret
        while xx<i:
            prev=ret
            ret=ret.next
            xx+=1
        prev.next=None
        prev=None
        return hello
    def size(self,l1):
        count=0
        while l1:
            count+=1
            l1=l1.next
        return count
obj=Solution()
print(obj.addTwoNumbers([2,4,3],[5,6,4]))