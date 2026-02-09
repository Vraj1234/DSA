class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        mx = float('-inf')
        pre, suf = 1,1
        for i, j in zip(range(n), range(n - 1, -1, -1)):
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1
            pre*=nums[i]
            suf*=nums[j]
            mx = max(mx, max(pre, suf))
        return mx
        