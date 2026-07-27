class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1]*C for _ in range(R)]

        def f(r,c):
            if r<0 or c<0:
                return 0
            if obstacleGrid[r][c] == 1:
                dp[r][c] = 0
                return 0
            if (r,c) == (0,0):
                dp[r][c] = 1
                return 1
            
            if dp[r][c] != -1:
                return dp[r][c]

            left = 0 if r-1<0 else f(r-1, c)
            top = 0 if c-1<0 else f(r, c-1)
            dp[r][c] = left + top
            return dp[r][c]
        
        return f(R-1, C-1)

