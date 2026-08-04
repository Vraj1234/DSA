class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[n] = True
        for i in range(n-1, -1, -1):
            for word in wordDict:
                wn = len(word)
                if i+wn<=n and s[i:i+wn] == word:
                    if dp[i+wn] == True:
                        dp[i] = True
                        break
        
        return dp[0]

        # def f(i):
        #     if i == n:
        #         return True
            
        #     if i>n:
        #         return False
            
        #     for word in wordDict:
        #         wn = len(word)
        #         if i+wn<=n and s[i:i+wn] == word:
        #             if f(i+wn):
        #                 return True
            
        #     return False
        
        # return f(0)
