class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        used = set()

        def bt(element, temp, used):
            if len(nums) == len(temp):
                res.append(temp[:])
                return
            
            for x in nums:
                if x not in used:
                    temp.append(x)
                    used.add(x)
                    bt(x, temp, used)
                    temp.pop()
                    used.discard(x)
        
        bt(nums[0], temp, used)
        return res

            