class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #memoization
        # def recur(n):
        #     if n<=1:
        #         return 0
            
        #     if dp[n]!= -1:
        #         return dp[n]

        #     left = recur(n-1) + cost[n-1]
        #     right = recur(n-2) + cost[n-2]
            
        #     dp[n] = min(left, right)
        #     return dp[n]
        
        # n= len(cost)
        # dp = [-1]*(n+1)
        # return recur(n)

        #Tabulation
        # n= len(cost)
        # dp = [-1]*(n+1)
        # dp[0], dp[1] = 0,0
        # for i in range(2, n+1):
        #     left = dp[i-1] + cost[i-1] 
        #     right = dp[i-2] + cost[i-2]
        #     dp[i] = min(left, right)
        
        # return dp[n]
    
        #Space optimization
        n= len(cost)
        p2, p1 = 0,0
        for i in range(2, n+1):
            left = p1 + cost[i-1] 
            right = p2 + cost[i-2]
            cur = min(left, right)
            p2 = p1
            p1 = cur
        
        return p1


            