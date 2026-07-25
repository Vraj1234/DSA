class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [None] * (n+1)
        def dfs(i):
            if i == n:
                dp[i] = True
                return dp[i]
            
            if i>n:
                return False

            if dp[i] != None:
                return dp[i]

            for word in wordDict:
                if i+len(word) <=n:
                    if word == s[i:i+len(word)]:
                        if dfs(i+len(word)):
                            dp[i] = True
                            return dp[i]
            dp[i] = False
            return dp[i]
        
        return dfs(0)
