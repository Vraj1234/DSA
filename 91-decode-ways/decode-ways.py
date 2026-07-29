class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1]*(n+1)
        def f(i):
            if i == n:
                dp[i] = 1
                return 1

            if s[i] == "0":
                return 0

            if dp[i] != -1:
                return dp[i]

            left = f(i+1)
            right = 0
            if i+1<n and 10<= int(s[i:i+2])<=26:
                right = f(i+2)
            
            dp[i] = left+right
            return left+right
        
        return f(0)