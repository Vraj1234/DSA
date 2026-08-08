class Solution:
    def trap(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0, n-1
        lmax, rmax = nums[l], nums[r]
        res = 0
        
        while l<r:

            if lmax<=rmax:
                l+=1
                lmax = max(lmax, nums[l])
                res += (lmax-nums[l])
            
            else:
                r-=1
                rmax = max(rmax, nums[r])
                res += (rmax-nums[r])
        
        return res