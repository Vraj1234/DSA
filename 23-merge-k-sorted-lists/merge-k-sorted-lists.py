# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        temp = ListNode()
        root = temp

        for i, n in enumerate(lists):
            if n:
                heapq.heappush(heap, (n.val, i, n))
        
        while heap:
            val, idx, node = heapq.heappop(heap)
            temp.next = node
            temp = temp.next 
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return root.next

