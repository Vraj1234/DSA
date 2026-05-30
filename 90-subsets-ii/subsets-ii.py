class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []

        def bt(start):
            res.append(temp[:])
            
            for idx in range(start, len(nums)):
                if idx > start and nums[idx] == nums[idx-1]:
                    continue
                temp.append(nums[idx])
                bt(idx+1)
                temp.pop()

        nums.sort()
        bt(0)
        return res