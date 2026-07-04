class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def HR1(arr):
            n = len(arr)
            if len(arr) == 1:
                return arr[0]
            
            # dp = [-1]*(n)
            p2 = arr[0]
            p1 = max(arr[0], arr[1])

            for i in range(2, n):
                pick = arr[i] + p2
                non_pick = p1
                curi = max(pick, non_pick)
                p2 = p1
                p1 = curi

            return p1

        m1 = HR1(nums[:-1])
        m2 = HR1(nums[1:])
        return max(m1, m2)
        