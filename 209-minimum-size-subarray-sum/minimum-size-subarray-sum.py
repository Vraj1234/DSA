class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        psum = 0
        l,r = 0,0
        res = float('inf')
        while r<n:
            while r<n and psum < target:
                psum+=nums[r]
                r+=1
            while l<n and psum >=target:
                res = min(res, r-l)
                psum-=nums[l]
                l+=1
        return 0 if res == float('inf') else res
