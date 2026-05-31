class Solution:
    def climbStairs(self, n: int) -> int:
        #Memoization
        # def recur(n):
        #     if n<=1:
        #         return 1
            
        #     if dp[n]!= -1:
        #         return dp[n]

        #     left = recur(n-1)
        #     right = recur(n-2)
        #     dp[n] = left+right
        #     return dp[n]
        
        # dp = [-1]*(n+1)
        # return recur(n)

        #Tabulation
        # dp = [-1]*(n+1)
        # dp[0], dp[1] =1,1
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]

        # return dp[n]

        #Space Optimization
        dp = [-1]*(n+1)
        p2, p1 =1,1
        for i in range(2, n+1):
            cur = p1 + p2
            p2 = p1
            p1 = cur

        return p1
