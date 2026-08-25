# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        dummy = ListNode()
        temp = dummy
        carry = 0
        s = 0
        while l1 or l2:
            v1 = 0 if not l1 else l1.val
            v2 = 0 if not l2 else l2.val
            s = v1 + v2 + carry
            carry = 0
            if s>9:
                s = s%10
                carry = 1
            temp.next = ListNode(s)
            temp = temp.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            temp.next = ListNode(1)
        
        return dummy.next

