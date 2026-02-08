class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = sys.maxsize
        def calc_hrs(t):
            hrs = 0
            for x in piles:
                hrs+= int(ceil(x/t))
            return hrs

        mx = max(piles)

        l,r = 1, mx

        while l<r:
            mid = (l+r)//2
            #print(l,r,mid, calc_hrs(mid))
            if calc_hrs(mid) <= h:
                r = mid
            else:
                l = mid+1         
        
        return l