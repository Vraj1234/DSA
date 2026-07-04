class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # dp = [-1]*(n)
        # def f(n):
        #     if n ==0:
        #         return nums[0]
        #     if n<0:
        #         return 0
        #     if dp[n] != -1:
        #         return dp[n]

        #     pick = nums[n]+ f(n-2)
        #     non_pick = 0 + f(n-1)
        #     dp[n] = max(pick, non_pick)
        #     return dp[n]
        
        # return f(len(nums)-1)

        # if len(nums) == 1:
        #     return nums[0]
        
        # dp = [-1]*(n)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, n):
        #     pick = nums[i] + dp[i-2]
        #     non_pick = dp[i-1]
        #     dp[i] = max(pick, non_pick)

        # return dp[n-1]

        if len(nums) == 1:
            return nums[0]
        
        # dp = [-1]*(n)
        p2 = nums[0]
        p1 = max(nums[0], nums[1])

        for i in range(2, n):
            pick = nums[i] + p2
            non_pick = p1
            curi = max(pick, non_pick)
            p2 = p1
            p1 = curi

        return p1