class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            minimum = float('inf')
            for diff in coins:
                temp = 0
                if i-diff < 0:
                    temp = float('inf')
                else:
                    temp = dp[i-diff]
                minimum = min(minimum, temp)
            dp[i] = 1 + minimum
        
        return dp[amount] if dp[amount] != float('inf') else -1

        # def f(n):
        #     if n == 0:
        #         return 1
        #     if n<0:
        #         return float('inf')
            
        #     if dp[n] != -1:
        #         return dp[n]

        #     minimum = float('inf')
        #     for diff in coins:

        #         minimum = min(minimum, f(n-diff))

        #     dp[n] = 1 + minimum
        #     return dp[n]
        
        # result = f(amount)
        # return -1 if result == float('inf') else result-1
