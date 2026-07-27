class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        R, C = m,n
        dp = [[-1]*C for _ in range(R)]
        dp[0][0] = 1
        for r in range(R):
            for c in range(C):
                if (r,c) == (0,0):
                    continue
                top = 0 if r-1<0 else dp[r-1][c]
                left = 0 if c-1<0 else dp[r][c-1]
                dp[r][c] = top+left
        return dp[R-1][C-1]

        # def f(r,c):
        #     if r<0 or c<0:
        #         return 0
        #     if r== 0 and c== 0:
        #         dp[r][c] = 1
        #         return dp[r][c]
            
        #     if dp[r][c] != -1:
        #         return dp[r][c]

        #     left = f(r, c-1)
        #     right = f(r-1, c)
        #     dp[r][c] = left+right
        #     return dp[r][c]
    
        # return f(R-1, C-1)

