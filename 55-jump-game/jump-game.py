class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n-1
        i = n-2
        while i>=0:
            print(target, i)
            if i+nums[i]>=target:
                target = i
            i-=1

        return target == 0
            