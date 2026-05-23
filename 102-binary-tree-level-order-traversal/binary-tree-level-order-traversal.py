# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        q.append(root)
        temp_node = []
        temp_val = []
        res = []
        while q:
            while q:
                temp_node.append(q.popleft())
            for element in temp_node:
                temp_val.append(element.val)
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            res.append(temp_val[:])
            temp_val.clear()
            temp_node.clear()
        return res

                
        