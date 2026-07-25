class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*(len(cost)+1)

        def f(n):
            if n == 0:
                return cost[0]
            if n == 1:
                return cost[1]
            
            if dp[n] != -1:
                return dp[n]

            left = f(n-1)
            right = f(n-2)
            res = min(left, right)
            dp[n] = res + cost[n] if n<len(cost) else res

            return dp[n]
        
        return f(len(cost))