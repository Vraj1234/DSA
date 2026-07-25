class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)

        def f(n):
            if n == 0:
                return 1
            if n<0:
                return float('inf')
            
            if dp[n] != -1:
                return dp[n]

            minimum = float('inf')
            for diff in coins:
                minimum = min(minimum, f(n-diff))

            dp[n] = 1 + minimum
            return dp[n]
        
        result = f(amount)
        return -1 if result == float('inf') else result-1
