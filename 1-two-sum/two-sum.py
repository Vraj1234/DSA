from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = defaultdict()
        for i,x in enumerate(nums):
            if target - x in freq:
                return [freq[target-x], i]
            else:
                freq[x] = i