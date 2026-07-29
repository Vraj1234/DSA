class Solution:
    def findContentChildren(self, greed: List[int], cookies: List[int]) -> int:
        greed = sorted(greed)
        cookies = sorted(cookies)

        g,c = 0,0
        res = 0
        while g<len(greed) and c<len(cookies):
            if greed[g]<=cookies[c]:
                g+=1
                c+=1
                res+=1
            else:
                c+=1
        
        return res
        