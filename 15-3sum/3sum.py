class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        n = len(nums)-1
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i - 1]:  
                continue
            l = i+1
            r = n
            while l<r:
                s = nums[l]+nums[r]+nums[i]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l+1] == nums[l]:
                        l+=1
                    while l<r and nums[r-1] == nums[r]:
                        r-=1
                    r-=1
                    l+=1
                elif s < 0:
                    l+=1
                else:
                    r-=1
        return res






