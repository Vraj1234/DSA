class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = [float('inf'),float('-inf')]

        def try_expanding(l,r):
            nonlocal res
            if r == -1:
                l,r = l,l
            
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1 > res[1]-res[0]+1:
                    res = [l,r]
                l-=1
                r+=1
        
        for i in range(len(s)):
            try_expanding(i,-1)

        #even
        l,r = 0,1
        while r<n:
            try_expanding(l,r)
            l+=1
            r+=1

        return s[res[0]:res[1]+1]