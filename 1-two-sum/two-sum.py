class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)
        for i,num in enumerate(nums):
            if target-num in map:
                return [i, map[target-num]]
            else:
                map[num] = i
        return [-1,-1]