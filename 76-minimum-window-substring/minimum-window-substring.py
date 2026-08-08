class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        n = len(s)
        l,r = 0,0
        check = Counter(t)
        cur = defaultdict(int)
        res = float('inf')
        res_idx = [-1, -1]
        match = 0

        while r<n:
            #expansion
            while r<n and match != len(check):
                if s[r] in check:
                    cur[s[r]]+=1
                    if cur[s[r]] == check[s[r]]:
                        match+=1
                r+=1

            #contraction
            while match == len(check):
                if r-l < res:
                    res = min(res, (r-l))
                    res_idx = [l,r]
                if s[l] in check:
                    cur[s[l]]-=1
                    if cur[s[l]] < check[s[l]]:
                        match-=1
                l+=1
        
        return s[res_idx[0]:res_idx[1]]



