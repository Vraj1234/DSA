# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = float('-inf')
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            total = left+right+root.val
            self.maximum = max(self.maximum, total)
            return max(root.val+left, root.val+right, 0)
        
        dfs(root)
        return self.maximum
