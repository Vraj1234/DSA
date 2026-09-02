class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]* (len(nums)+1)
        def f(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            if dp[i] != -1:
                return dp[i]

            pick = nums[i] + f(i-2)
            not_pick = 0 + f(i-1)
        
            dp[i] = max(pick, not_pick)
            return max(pick, not_pick)
        
        return f(len(nums)-1)