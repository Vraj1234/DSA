# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        heap = []
        d = ListNode()
        root = d
        for i,x in enumerate(lists):
            if x:
                heapq.heappush(heap, (x.val, i, x))
        
        while heap:
            val, idx, ptr = heapq.heappop(heap)
            if ptr.next:
                heapq.heappush(heap, (ptr.next.val, idx, ptr.next))
            d.next = ptr
            d = d.next
        
        if d == root:
            return None
        else:
            return root.next
        