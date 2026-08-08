# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        first = True

        def reverse(root): 
            prev = None
            cur = root
            nxt = root.next
            while cur:
                cur.next = prev
                prev = cur
                cur = nxt
                if nxt:
                    nxt = nxt.next
            return prev

        if k == 1:
            return head

        next_node = head
        while True:
            start = next_node
            temp = next_node
            if not temp:
                return h
            i = 0
            while i<k-1:
                temp = temp.next
                if not temp:
                    prev.next = start
                    return h
                i+=1

            
            next_node = temp.next
            temp.next = None
            v = reverse(start)
            if first:
                h = v
                first = False
            else:
                prev.next = temp
            prev = start
        




