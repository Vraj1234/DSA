class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2

        l,r = 1,1
        ctr = 1
        while r<len(nums):
            if nums[r] == nums[r-1]:
                r+=1
            else:
                nums[l] = nums[r]
                l+=1  
                ctr+=1  
                r+=1
        
        return ctr
        