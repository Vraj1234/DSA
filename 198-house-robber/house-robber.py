class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return max(nums)

        p1, p2 = nums[0], max(nums[0], nums[1])
        for i in range(2, n+1):
            if i<n:
                res = max(p2, p1 + nums[i])
            else:
                res = max(p2, p1)
            p1 = p2
            p2 = res
        return p2

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