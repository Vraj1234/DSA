# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
        def dfs(root):
            
            if root.left:
                adj[root.val].append(root.left.val)
                adj[root.left.val].append(root.val)
                dfs(root.left)

            if root.right:
                adj[root.val].append(root.right.val)
                adj[root.right.val].append(root.val)
                dfs(root.right)
        
        dfs(root)
        q = deque()
        vis = set()
        q.append(target.val)
        vis.add(target.val)
        depth = 0
        level = []

        while q:
            for i in range(len(q)):
                node = q.popleft()
                level.append(node)
                for nei in adj[node]:
                    if nei not in vis:
                        q.append(nei)
                        vis.add(nei)
            depth+=1
            if depth == k+1:
                return level
            level.clear()
        
        return level

