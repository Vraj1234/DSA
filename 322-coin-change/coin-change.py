class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)

        def f(amount):
            if amount == 0:
                return 0
            
            if amount < 0:
                return float('inf')

            if dp[amount]!= -1:
                return dp[amount]

            res = float('inf')
            for coin in coins:
                val = f(amount-coin)
                res = min(res, val)
            
            dp[amount] = 1+ res
            return 1+ res

        result = f(amount)

        return -1 if result == float('inf') else result