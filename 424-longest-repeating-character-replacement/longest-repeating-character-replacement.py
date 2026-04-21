class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        n = len(s)
        map = defaultdict(int)
        res = 0
        max_freq = 0
        while r < n:
            map[s[r]]+=1
            max_freq = max(max_freq, map[s[r]])

            if (r-l+1) - max_freq >k:
                map[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
            r+=1
        
        return res
