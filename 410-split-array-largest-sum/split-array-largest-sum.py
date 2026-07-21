class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        ans = l
    
        def numSubarrays(val):
            s = 0
            res = 0
            for num in nums:
                s+= num
                if s > val:
                    res+=1
                    s = num
            if s!= 0:
                res+=1

            return res


        while l<=r:
            mid = l + ((r-l)//2)
            subarrays = numSubarrays(mid)
            if subarrays <= k:
                ans = mid
                r = mid-1
            else:
                l = mid+1

        return ans