"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        start = Node(node.val)

        matching = {}
        matching[node] = start

        original_q = deque()
        new_q = deque()
        original_q.append(node)
        new_q.append(start)

        while original_q:
            og = original_q.popleft()
            temp = new_q.popleft()
            for nei in og.neighbors:
                if nei not in matching:
                    original_q.append(nei)
                    new_node = Node(nei.val)
                    new_q.append(new_node)
                    temp.neighbors.append(new_node)
                    matching[nei] = new_node
                else:
                    temp.neighbors.append(matching[nei])

        return start 