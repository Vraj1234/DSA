class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        R,C = m,n
        dp = [[-1]*C for _ in range(R)]
        def f(r,c):
            if r==0 and c ==0:
                return 1
            if r<0 or c<0:
                return 0

            if dp[r][c] != -1:
                return dp[r][c]

            top = f(r-1,c)
            left = f(r,c-1)

            dp[r][c] = top+left

            return dp[r][c]

        return f(R-1, C-1)