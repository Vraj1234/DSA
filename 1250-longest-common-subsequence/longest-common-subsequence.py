class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        R,C = len(s1), len(s2)
        dp = [[None]*(C+1) for _ in range(R+1)]
        for r in range(R+1):
            for c in range(C+1):
                if r== 0 or c==0:
                    dp[r][c] = 0
        
        for r in range(1,R+1):
            for c in range(1, C+1):
                if s1[r-1] == s2[c-1]:
                    v = 1 + dp[r-1][c-1]
                    dp[r][c] = v
                    continue
                t = 0 + max(dp[r-1][c],dp[r][c-1])
                dp[r][c] = t

        return dp[R][C]

        # def f(i,j):
        #     if i==0 or j==0:
        #         return 0

        #     if dp[i][j] != None:
        #         return dp[i][j]

        #     if s1[i-1] == s2[j-1]:
        #         v = 1 + f(i-1, j-1)
        #         dp[i][j] = v
        #         return v
            
        #     t = 0 + max(f(i-1,j),f(i,j-1))
        #     dp[i][j] = t
        #     return t

        # return f(R,C)