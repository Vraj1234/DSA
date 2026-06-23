class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, a):
        if self.parent[a] == a:
            return a
        
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, x,y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return False

        if self.rank[px] == self.rank[py]:
            self.parent[py] = px
            self.rank[px] +=1
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
        
        return True
    
    
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        d = DSU(n)
        res = n

        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j] == 1:
                    if d.union(i,j):
                        res-=1
        return res

        