class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [None] * (n+1)
        
        def f(i):
            if i == n:
                dp[i] = True
                return True
            if i>n:
                return False 

            if dp[i] != None:
                return dp[i]

            for word in wordDict:
                w = len(word)
                if s[i:i+w] == word:
                    if f(i+w):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        
        return f(0)


