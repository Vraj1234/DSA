class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l=r=0
        res = 0
        n = len(nums)  
         
        while r<n-1:
            farthest = float('-inf')  
            for i in range(l,r+1):
                farthest = max(farthest, i + nums[i])
            l = r+1
            r = farthest
            res+=1
        
        return res
