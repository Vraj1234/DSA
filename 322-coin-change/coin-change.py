class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]* (amount+1)
        def f(n):
            if n == 0:
                dp[n] = 0
                return 0
            if n<0:
                return float('inf')
            
            if dp[n] != -1:
                return dp[n]

            res = float('inf')
            for coin in coins:
                res = min(res, f(n-coin))
            
            dp[n] = 1+res
            return dp[n]
        
        res = f(amount)
        return -1 if res == float('inf') else res
