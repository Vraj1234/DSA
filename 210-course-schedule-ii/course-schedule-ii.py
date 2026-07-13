class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        indegree = [0]*n
        adj = defaultdict(list)
        res = []
        
        for e,s in prerequisites:
            adj[s].append(e)
            indegree[e]+=1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node = q.popleft()
            res.append(node)
            for neighbor in adj[node]:
                indegree[neighbor]-=1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(res) == n:
            return res
        else:
            return []
