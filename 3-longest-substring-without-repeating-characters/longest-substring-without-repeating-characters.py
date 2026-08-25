class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l,r = 0,0
        n = len(s)
        res = 0
        while r<n:
            while r<n and s[r] not in seen:
                seen.add(s[r])
                r+=1
            res = max(res, (r-l))
            while l<n and r<n and s[l] != s[r]:
                seen.remove(s[l])
                l+=1
            seen.remove(s[l])
            l+=1
        return res
             
            
        