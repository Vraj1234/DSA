class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = r= 0
        s = 0
        res = float('-inf')
        while r<k:
            s+=nums[r]
            r+=1
        
        n = len(nums)
        res = max(res, float(s/k))
        # print(l,r)
        while r<n:
            # print(nums[l:r])
            res = max(res, float(s/k))
            s-=nums[l]
            l+=1
            s+=nums[r]
            r+=1

        res = max(res, float(s/k))
        return res
