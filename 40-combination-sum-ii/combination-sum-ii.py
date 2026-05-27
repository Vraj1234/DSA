class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        temp = []
        candidates.sort()

        def bt(start, nums, temp, s):
            if s == target:
                res.append(temp[:])
                return
            else:
                for i in range(start, len(nums)):
                    if i > start and  nums[i] == nums[i-1]:
                        continue
                    if s + nums[i] > target:
                        break
                    s+=nums[i]
                    temp.append(nums[i])
                    bt(i+1, nums, temp, s)
                    s-=nums[i]
                    temp.pop()

        
        bt(0, candidates, temp, 0)
        return res