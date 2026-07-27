class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        R, C = m,n
        dp = [[-1]*C for _ in range(R)]

        def f(r,c):
            if r<0 or c<0:
                return 0
            if r== 0 and c== 0:
                dp[r][c] = 1
                return dp[r][c]
            
            if dp[r][c] != -1:
                return dp[r][c]

            left = f(r, c-1)
            right = f(r-1, c)
            dp[r][c] = left+right
            return dp[r][c]
    
        return f(R-1, C-1)