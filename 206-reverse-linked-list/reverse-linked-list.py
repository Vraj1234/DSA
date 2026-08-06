# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        prev = None
        cur = head
        next = head.next

        while cur:
            cur.next = prev
            prev = cur
            cur = next
            if next:
                next = next.next
        
        return prev