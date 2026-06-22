class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height)-1
        lmax, rmax = height[0], height[-1]

        while l<r:
            if lmax<=rmax:
                l+=1
                if height[l]<=lmax:
                    res= res+(lmax - height[l])
                lmax = max(lmax, height[l])
            else:
                r-=1
                if height[r]<=rmax:
                    res= res+(rmax - height[r])
                rmax = max(rmax, height[r])
        
        return res