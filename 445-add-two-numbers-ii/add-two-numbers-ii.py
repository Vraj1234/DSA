# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []
        carry = 0
        nxt = None
        head = None
        t1 = l1
        t2 = l2
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        l1 = t1
        l2 = t2
        while s1 or s2 or carry:
            s = carry
            if s1:
                s+=s1.pop()
            if s2:
                s+= s2.pop()
            
            if not nxt:
                nxt = ListNode(s%10)
            else:
                new_node = ListNode(s%10)
                new_node.next = nxt
                nxt = new_node
            
            head = nxt
            carry = s//10
        
        return head

