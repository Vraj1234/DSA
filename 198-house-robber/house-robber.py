class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            max(nums[0], nums[1])
        dp = [-1]*(n+1)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n+1):
            left = dp[i-1] 
            right = 0
            if i<n:
                right = nums[i] + dp[i-2]
            dp[i] = max(left,right)

        return dp[n]
        # def f(i):
        #     if i == 0:
        #         return nums[0]
            
        #     if i == 1:
        #         return max(nums[0], nums[1])
            
        #     if i<0:
        #         return float('-inf')

        #     left = f(i-1)
        #     right = 0
        #     if i<n:
        #         right = nums[i] + f(i-2)
        
        #     return max(left, right)
        
        # return f(len(nums))