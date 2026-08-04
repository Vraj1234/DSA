class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        res = 0
        for i in range(len(nums)):
            s += nums[i]
            if s<0:
                s = 0
            res = max(res, s)
        
        if res== 0:
            return max(nums)
        else:
            return res
        
