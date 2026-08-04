class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        
        def f(i):
            if i<0:
                return float('inf')
                
            if i == 0:
                dp[i] = 0
                return 0

            if dp[i] != -1:
                return dp[i]

            res = float('inf')
            for idx in range(len(coins)):
                res = min(res, f(i-coins[idx]))
            
            dp[i] = 1+res
            return 1+res
        
        result = f(amount)
        return -1 if result ==float('inf') else result