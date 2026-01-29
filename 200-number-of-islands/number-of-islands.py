class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        vis = [[False]*cols for _ in range(rows)]
        print(vis)

        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or vis[i][j] == True or grid[i][j] == "0":
                return
            
            vis[i][j] = True
            dfs(i, j-1)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i+1, j)
    
        ctr = 0

        for i in range(rows):
            for j in range(cols):
                if(not vis[i][j] and grid[i][j] == "1"):
                    dfs(i,j)
                    ctr+=1
        
        return ctr