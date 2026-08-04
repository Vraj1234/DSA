class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            res = float('inf')
            for idx in range(len(coins)):
                val = float('inf') if i-coins[idx]<0 else dp[i-coins[idx]]
                res = min(res, val)
            dp[i] = 1+res
        return dp[amount] if dp[amount] != float('inf') else -1

        # def f(i):
        #     if i<0:
        #         return float('inf')
                
        #     if i == 0:
        #         dp[i] = 0
        #         return 0

        #     if dp[i] != -1:
        #         return dp[i]

        #     res = float('inf')
        #     for idx in range(len(coins)):
        #         res = min(res, f(i-coins[idx]))
            
        #     dp[i] = 1+res
        #     return 1+res
        
        # result = f(amount)
        # return -1 if result ==float('inf') else result