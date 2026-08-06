class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def find(nums):
            s = 0
            for i in range(len((nums))):
                s+=nums[i][1]
            s = ceil(s/2)
            running_sum = 0
            for i,c in enumerate(nums):
                running_sum+=c[1]
                if running_sum>=s:
                    return i
            return -1
        
        new = [(nums[i], cost[i]) for i in range(len(nums))]
        new.sort()
        idx = find(new)
        target = new[idx][0]
        res = 0
        for element in new:
            num, c = element
            res+= abs(target-num)*c
        
        return res

