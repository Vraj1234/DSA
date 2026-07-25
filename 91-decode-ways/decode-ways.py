class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1]*(n+1)

        def f(i): 
            if i >= n:
                return 1

            if s[i] == "0":
                return 0

            if dp[i] != -1:
                return dp[i]

            left = f(i+1)
            right = 0
            if i+1<n:
                temp = s[i:i+2]
                num = int(temp)
                if 10<= num <=26:
                    right = f(i+2)

            dp[i] = left+right
            return dp[i]
        
        result = f(0)
        # print("Filled DP Array:", dp)  # <--- Print AFTER f(0) finishes
        return result