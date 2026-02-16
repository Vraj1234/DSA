class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        umap = defaultdict()
        for i,x in enumerate(nums):
            if target-x not in umap:
                umap[x] = i
            else:
                return [i, umap[target-x]]