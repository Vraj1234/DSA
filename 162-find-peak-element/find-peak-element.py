class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        n = len(nums)-1
        l,r = 0, n

        while l<=r:
            mid = l + ((r-l)//2)
            if 1<=mid<=n-1 and nums[mid-1] < nums[mid]  and nums[mid] > nums[mid+1]:
                return mid
            elif mid == 0 and nums[mid] > nums[mid+1]:
                return mid
            elif mid == n and nums[mid-1] < nums[mid]:
                return mid
            elif nums[mid+1] > nums[mid]:
                l=mid+1
            else:
                r=mid-1

        return -1