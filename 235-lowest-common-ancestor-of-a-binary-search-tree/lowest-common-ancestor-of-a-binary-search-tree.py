# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val = p.val
        q_val = q.val
        while root:
            if (min(p_val, q_val) < root.val < max(p_val, q_val)) or (root.val == p_val) or (root.val == q_val):
                return root
            if root.val < p_val and root.val < q_val:
                root = root.right
            if root.val > p_val and root.val > q_val:
                root = root.left