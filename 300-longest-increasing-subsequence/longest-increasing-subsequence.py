class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1]*(n+1) for _ in range (n+1)]
        # for i range(len(dp[-1])):
        #     dp[-1][i] = 0

        def f(i, prev):
            if i == n:
                return 0

            if dp[i][prev] != -1:
                return dp[i][prev]

            not_pick = 0 + f(i+1, prev)
            pick = 0
            if (prev == -1)or (nums[i]>nums[prev]):
                pick = 1+ f(i+1, i)
            
            dp[i][prev] = max(not_pick, pick)
            return dp[i][prev]
        
        return f(0, -1)
        