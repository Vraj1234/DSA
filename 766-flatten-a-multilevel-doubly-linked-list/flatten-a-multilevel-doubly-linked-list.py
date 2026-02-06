"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        stack = []
        last = None
        temp = head
        while True:
            while temp:
                last = temp
                if temp.child: #if there is a child
                    if temp.next:
                        stack.append(temp.next)
                    temp.next = temp.child
                    child = temp.child
                    child.prev = temp
                    temp.child = None
                temp = temp.next

            if len(stack) == 0:
                break
            else:

                temp = last
                temp.next = stack[-1]
                rejoin = stack[-1]
                rejoin.prev = temp
                stack.pop()
                temp = temp.next

            #perform logic when temp is null
            #strcutre while loop to exit correctly

        return head
        