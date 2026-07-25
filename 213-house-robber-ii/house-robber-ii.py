class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def get_cost(ls):
            n = len(ls)
            if n == 0:
                return 0
            if n<3:
                return max(ls)
            p1, p2 = ls[0], max(ls[0], ls[1])
            for i in range(2, n+1):
                if i < n:
                    res = max(p2, p1 + ls[i])
                else:
                    res = max(p2, p1)
                p1 = p2
                p2 = res
            return p2
        
        return max(get_cost(nums[:-1]), get_cost(nums[1:]))