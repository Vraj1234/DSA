class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        cnt = 0
        res = 0
        for num in seen:
            if num-1 not in seen:
                val = num
                while val in seen:
                    cnt+=1
                    val+=1
                res = max(res, cnt)
                cnt = 0
        return res



