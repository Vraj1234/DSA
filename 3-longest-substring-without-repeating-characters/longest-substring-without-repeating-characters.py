class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l,r = 0,0
        res = 0
        while r<len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            seen.add(s[r])
            res = max(res, len(seen))
            r+=1
        return res