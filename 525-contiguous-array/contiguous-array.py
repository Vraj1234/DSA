class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = defaultdict(int)
        ptr = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ptr+=1
            else:
                ptr-=1

            if ptr in map:
                res = max(res, i-map[ptr])
            elif ptr==0:
                res = max(res, i+1)
            else:
                map[ptr] = i
        
        return res