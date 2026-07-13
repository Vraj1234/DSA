class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = defaultdict(set)
        indegree = defaultdict(int)

        for t in trust: #O(t)
            a,b = t
            adj[a].add(b)
            indegree[b] +=1
        
        candidates = []

        for i in range(1,n+1): #O(n)
            if len(adj[i]) == 0:
                candidates.append(i)
        
        for c in candidates: #O(c)
            if indegree[c] == n-1:
                return c
        
        return -1

        #O(t) + O(n) + O(c)