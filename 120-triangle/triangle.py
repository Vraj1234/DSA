class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[-1]*i for i in range(1,n+1)]
        for i in range(len(triangle[-1])):
            dp[-1][i] = triangle[-1][i]
        
        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                bottom = triangle[i][j] + dp[i+1][j]
                bottom_right = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(bottom, bottom_right)
        
        return dp[0][0]
        
        # def f(r,c):
        #     if r == n-1:
        #         dp[r][c] = triangle[r][c]
        #         return dp[r][c]
            
        #     if r >=n:
        #         return float('inf')
            
        #     if dp[r][c] != -1:
        #         return dp[r][c]

        #     left = triangle[r][c] + f(r+1, c)
        #     right = triangle[r][c] + f(r+1, c+1)

        #     dp[r][c] = min(left, right)
        #     return dp[r][c]
        
        # return f(0,0)
