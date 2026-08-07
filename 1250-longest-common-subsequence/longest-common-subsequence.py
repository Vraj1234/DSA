class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n,m = len(s1), len(s2)
        dp = [[None]*(m+1) for _ in range(n+1)]


        def f(i,j):
            if i==0 or j==0:
                return 0

            if dp[i][j] != None:
                return dp[i][j]

            if s1[i-1] == s2[j-1]:
                v = 1 + f(i-1, j-1)
                dp[i][j] = v
                return v
            
            t = 0 + max(f(i-1,j),f(i,j-1))
            dp[i][j] = t
            return t

        return f(n,m)