class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = defaultdict(int)
        map[0] = 1
        prefix_sum = 0
        res = 0
        for num in nums:
            prefix_sum+=num
            if prefix_sum-k in map:
                res+=map[prefix_sum-k]
            map[prefix_sum]+=1
        return res
