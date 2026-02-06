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
        
        q = deque([root])
        res = []

        while q:
            temp = []
            val = []
            while q:
                t = q[0]
                q.popleft()
                temp.append(t.val)
                val.append(t)
            res.append(temp)
            for e in val:
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
        
        return res
