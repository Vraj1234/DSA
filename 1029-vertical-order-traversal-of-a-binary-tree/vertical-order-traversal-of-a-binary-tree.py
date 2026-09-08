# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((root, 0))
        buckets = defaultdict(list)
        min_val, max_val = float('inf'), float('-inf')
        depth = 0
        while q:
            for i in range(len(q)):
                node, bucket = q.popleft()
                buckets[bucket].append((node.val, depth))
                #print(buckets)
                min_val = min(min_val, bucket)
                max_val = max(max_val, bucket)
                if node.left:
                    q.append((node.left, bucket-1))
                if node.right:
                    q.append((node.right, bucket+1))
            depth+=1
        

        res = []
        for i in range(min_val, max_val+1):
            ls = buckets[i]
            ls.sort(key = lambda x: (x[1], x[0]))
            res.append([node for node, depth in ls])
        
        return res
