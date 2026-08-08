class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)< len(s1):
            return False

        cur = defaultdict(int)
        l,r = 0, 0
        check = Counter(s1)
        
        while r<len(s1):
            cur[s2[r]]+=1
            r+=1
        r-=1

        if check == cur:
            return True

        while r<len(s2):
            #print(s1, s2[l:r+1])
            if check == cur:
                return True
            cur[s2[l]]-=1
            if cur[s2[l]] == 0:
                del cur[s2[l]]
            l+=1
            r+=1
            if r<len(s2):
                cur[s2[r]]+=1
        
        return False

