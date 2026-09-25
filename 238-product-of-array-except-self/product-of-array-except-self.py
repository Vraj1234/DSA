class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]
        for i in range(len(nums)):
            prefix.append(nums[i]* prefix[-1])
        # print(prefix)
        suffix = [1] 
        for i in range(len(nums)-1, -1, -1):
            suffix.append(nums[i] * suffix[-1])
        suffix.reverse()
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i+1])
        return res