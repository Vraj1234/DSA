class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return max(nums)
        dp = [-1] * (n+1)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n+1):
            if i<n:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            else:
                dp[i] = max(dp[i-1], dp[i-2])
        return dp[n]

        # def f(n):
        #     if n == 0:
        #         return nums[0]
        #     if n == 1:
        #         return max(nums[0], nums[1])

        #     if dp[n] != -1:
        #         return dp[n]
        #     left = f(n-1) + 0
        #     right = f(n-2) + nums[n]
        #     dp[n] = max(left, right)
        #     return dp[n]

        # return f(len(nums)-1)