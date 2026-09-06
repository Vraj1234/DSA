class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        target = Counter(t)
        match = 0
        n = len(s)
        map = defaultdict(int)
        res = float('inf')
        res_word = ""
        
        while r<n:
            while r<n and match != len(target):
                if s[r] in target:
                    map[s[r]]+=1
                    if map[s[r]] == target[s[r]]:
                        match+=1
                r+=1

            while l<r and match == len(target):
                if r-l< res:
                    res = r-l
                    res_word = s[l:r]
                if s[l] in map:
                    map[s[l]]-=1
                    if map[s[l]] < target[s[l]]:
                        match-=1
                l+=1
                
        return res_word
                
