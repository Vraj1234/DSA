class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dp = [[-1]*C for _ in range(R)]

        def f(r,c):
            if (r,c) == (0,0):
                dp[r][c] = grid[r][c] 
                return grid[r][c]
            if r<0 or c<0:
                return float('inf')
            
            if dp[r][c] != -1:
                return dp[r][c]
            left = grid[r][c] + f(r-1, c)
            top = grid[r][c] + f(r, c-1)
            dp[r][c] = min(left, top)
            return dp[r][c]
        
        return f(R-1, C-1)