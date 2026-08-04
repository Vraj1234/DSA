class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        # dp[0], dp[1] = 

        def f(i):
            if i == 0 or i == 1:
                dp[i] = 1
                return 1
            
            if dp[i] != -1:
                return dp[i]

            left = f(i-1)
            right = f(i-2)

            dp[i] = left+right
            return left+right
        
        return f(n)