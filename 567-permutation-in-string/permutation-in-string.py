class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        c = Counter(s1)
        l,r = 0, len(s1)-1
        freq = defaultdict(int)
        for x in range(l,r+1):
            freq[s2[x]]+=1

        while r < len(s2):
            print(freq)
            print(c)
            if(freq == c):
                return True
            if freq[s2[l]] == 1:
                del freq[s2[l]]
            else:
                freq[s2[l]]-=1
            l+=1
            r+=1
            if r< len(s2): 
                freq[s2[r]]+=1
        return False
