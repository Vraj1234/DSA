# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        cur = head
        after = head.next
        prev = None

        while cur:
            cur.next, prev, cur = prev, cur, after
            if after!=None:
                after = after.next
        
        return prev
        