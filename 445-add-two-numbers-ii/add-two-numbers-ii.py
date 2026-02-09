# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def rev(l):
            if l is None:
                return None
            if l.next is None:
                return l
            if l.next.next is None:
                n = l.next
                l.next = None
                n.next = l
                return n
            c = l.next
            p = l
            n = l.next.next
            p.next = None
            c.next = p
            while n is not None:
                c.next = p
                p = c
                c = n
                n = n.next
            c.next = p
            return c
        
        rl1 = rev(l1)
        rl2 = rev(l2)

        carry = 0
        head = ListNode(-1)
        temp = head
        while rl1 or rl2: #v1 = 0, v2 = 0, carry = 0
            v1 = rl1.val if rl1 else 0
            v2 = rl2.val if rl2 else 0
            s = v1+ v2 + carry #7
            if carry:
                carry = 0
            if s>9:
                s = s%10 #s = 0
                carry = 1
            temp.next = ListNode(s)
            temp = temp.next
            if rl1:
                rl1 = rl1.next
            if rl2:
                rl2 = rl2.next
            
        if carry:
            temp.next = ListNode(carry)
            temp = temp.next
        print(head.next)
        return rev(head.next)
    

