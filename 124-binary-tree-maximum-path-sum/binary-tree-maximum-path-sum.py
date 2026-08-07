# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def postorder(root):
            nonlocal res
            if not root:
                return 0
            
            left = postorder(root.left)
            if left<=0:
                left = 0
            right = postorder(root.right)
            if right<=0:
                right = 0
            res = max(res, root.val + left + right)
            return root.val + max(left, right)
        
        postorder(root)
        return res


        
