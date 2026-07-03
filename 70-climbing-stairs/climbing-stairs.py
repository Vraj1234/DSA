class Solution:
    def climbStairs(self, n: int) -> int:
        # Memoization
        # dp = [-1] * (n+1)
        # def f(n):
        #     if n <=1:
        #         return 1
            
        #     if dp[n] != -1:
        #         return dp[n]
            
        #     dp[n] = f(n-1) + f(n-2)
        #     return dp[n]
        
        # return f(n)
    
        dp = [-1]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]