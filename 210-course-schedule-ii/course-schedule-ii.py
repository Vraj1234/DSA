class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0]*numCourses

        for d,s in prerequisites:
            adj[s].append(d)
            indegree[d]+=1

        q = deque()
        vis = set()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
                vis.add(i)
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for neighbor in adj[node]:
                if neighbor not in vis:
                    indegree[neighbor]-=1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
                        vis.add(neighbor)
        
        if numCourses == len(res):
            return res
        else:
            return []