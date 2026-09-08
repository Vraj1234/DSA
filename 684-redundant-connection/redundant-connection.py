class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = defaultdict(int)
        rank = defaultdict(int)
        n = len(edges)

        for i in range(1,n+1):
            parent[i] = i
            rank[i] = 0

        def union(a,b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False
            if rank[pa] == rank[pb]:
                parent[pb] = pa
                rank[pa]+=1
            elif rank[pa] < rank[pb]:
                parent[pa] = pb
            else:
                parent[pb] = pa
            return True
        
        def find(a):
            if parent[a] == a:
                return a
            parent[a]= find(parent[a])
            return parent[a]
    
        for s,d in edges:
            if not union(s,d):
                return [s,d]
        
        return []
