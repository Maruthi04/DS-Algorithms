class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        dic=dict()
        while headA:
            dic[headA]=headA
            headA=headA.next
        while headB:
            if headB in dic:
                return headB
            headB=headB.next
        return
