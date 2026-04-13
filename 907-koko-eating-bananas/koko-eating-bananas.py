class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def is_valid(mid, h):
            hrs = 0
            for x in piles:
                hrs+=int(ceil(x/mid))
            return hrs<=h

        while l<=r:
            mid = (l+r)//2
            if is_valid(mid, h):
                r = mid-1
            else:
                l = mid+1
        return l