class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        vis = set()
        res = 0
        self.area = 0
        
        def dfs(r,c):
            if r<0 or c<0 or r >=rows or c>=cols or (r,c) in vis or grid[r][c] == 0:
                return

            vis.add((r,c))
            self.area+=1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in vis:
                    self.area = 0
                    dfs(r,c)
                    print(self.area)
                    res=max(res, self.area)
                    self.area = 0
        
        return res