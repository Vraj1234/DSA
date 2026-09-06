class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l,r):
            # print("Entering")
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1
            # print("exiting")
            return

        n = len(nums)
        if k>len(nums):
            k = k%n
        
        reverse(n-k, n-1)
        reverse(0, n-k-1)
        reverse(0, n-1)
        return
        