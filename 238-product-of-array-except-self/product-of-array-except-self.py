class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = list(accumulate(nums, mul))
        suffix = list(accumulate(nums[::-1], mul))[::-1]
        res = []
        for i,x in enumerate(nums):
            l = 1 if i-1<0 or i-1>=n else prefix[i-1]
            r = 1 if i+1<0 or i+1>=n else suffix[i+1]
            res.append(l*r)
        return res
