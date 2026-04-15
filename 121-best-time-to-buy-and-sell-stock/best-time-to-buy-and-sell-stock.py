class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_max = list(accumulate(prices[::-1], max))[::-1]
        res = 0
        for i,x in enumerate(prices):
            res = max(res, p_max[i]-x)

        return res