class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ctr = 0

        def try_expanding(l,r):
            nonlocal ctr
            if r == -1:
                l, r = l, l
            while l>=0 and r<n and s[l] == s[r]:
                ctr+=1
                l-=1
                r+=1            

        #odd
        i = 0
        while i<n:
            try_expanding(i,-1)
            i+=1
        #even
        i,j = 0,1
        while j<n:
            try_expanding(i,j)
            i+=1
            j+=1
        
        return ctr