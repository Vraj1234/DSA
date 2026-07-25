class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        
        def try_expanding(l,r):
            nonlocal res
            if r == -1:
                l,r = l, l
            
            while l>=0 and r<n and s[l] == s[r]:
                res+=1
                l-=1
                r+=1

        #odd
        for i in range(n):
            try_expanding(i, -1)

        #even
        if n>1:
            l, r = 0, 1
            while r<n:
                try_expanding(l,r)
                l+=1
                r+=1
        
        return res
