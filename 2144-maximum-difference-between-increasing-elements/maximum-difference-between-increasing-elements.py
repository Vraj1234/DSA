class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        mn = float('inf')
        res = float('-inf')
        for i in range(len(nums)):
            if nums[i] <= mn:
                mn = nums[i]
            else:
                res = max(res, nums[i]-mn)
        return -1 if res == float('-inf') else res
