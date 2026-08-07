class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(len(nums)):
            l,r = i+1, n-1
            
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.add((nums[i],nums[l],nums[r]))
                    while l<r and nums[l+1] == nums[l]:
                        l+=1
                    while l<r and nums[r-1] == nums[r]:
                        r-=1
                    l+=1
                    r-=1
                elif s<0:
                    l+=1
                else:
                    r-=1
        return [list(x) for x in res]
        