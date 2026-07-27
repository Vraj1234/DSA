class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dp = [[-1]*C for _ in range(R)]
        dp[0][0] = grid[0][0]
        for r in range(R):
            for c in range(C):
                if r == 0 and c == 0:
                    continue
                left = float('inf') if r-1<0 else grid[r][c] + dp[r-1][c]
                top = float('inf') if c-1<0 else grid[r][c] + dp[r][c-1]
                dp[r][c] = min(left, top)
        return dp[R-1][C-1]
                

        # def f(r,c):
        #     if (r,c) == (0,0):
        #         dp[r][c] = grid[r][c] 
        #         return grid[r][c]
        #     if r<0 or c<0:
        #         return float('inf')
            
        #     if dp[r][c] != -1:
        #         return dp[r][c]
        #     left = grid[r][c] + f(r-1, c)
        #     top = grid[r][c] + f(r, c-1)
        #     dp[r][c] = min(left, top)
        #     return dp[r][c]
        
        # return f(R-1, C-1)