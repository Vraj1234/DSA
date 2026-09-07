class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psum = 0
        map = defaultdict(int)
        map[0] = 1
        res = 0
        for i in range(len(nums)):
            psum += nums[i]
            if psum - k in map:
                res += map[psum - k]
            map[psum]+=1
        
        return res