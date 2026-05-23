# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.bad = 0
        self.total = 0
        def dfs(root, mx):
            if not root:
                return
            if root.val < mx:
                self.bad-=1
            if root.val > mx:
                mx = root.val
            self.total +=1
            dfs(root.left, mx)
            dfs(root.right, mx)
        
 

        dfs(root, root.val)
        return self.total + self.bad
        