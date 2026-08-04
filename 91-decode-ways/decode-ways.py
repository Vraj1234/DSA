class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1]*(n+1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            left = dp[i+1]
            right = 0
            if i+1<n and 10<=int(s[i:i+2])<=26:
                right = dp[i+2]
            dp[i] = left+right
        return dp[0]
            
        # def f(i):
        #     if i == n:
        #         return 1
            
        #     if i >= n:
        #         return 0

        #     if s[i] == "0":
        #         return 0

        #     left = f(i+1)
        #     right = 0
        #     if i+1<n and 10<=int(s[i:i+2])<=26:
        #         right = f(i+2)
            
        #     return left+right

        # return f(0)