class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*(n+1)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2,n+1):
            dp[i] = min(dp[i-1], dp[i-2])
            if i<n:
                dp[i] += cost[i]
        
        return dp[n]
            

        # def f(n):
        #     if n == 0:
        #         return cost[0]
        #     if n == 1:
        #         return cost[1]
            
        #     if dp[n] != -1:
        #         return dp[n]

        #     left = f(n-1)
        #     right = f(n-2)
        #     res = min(left, right)
        #     dp[n] = res + cost[n] if n<len(cost) else res

        #     return dp[n]
        
        return f(len(cost))