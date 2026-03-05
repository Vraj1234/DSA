class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        i = 0
        temp =[]
        res = []
        n = len(nums)
        def rec(i, nums, temp):
            if i == n:
                res.append(temp[:])
                return
            
            rec(i+1, nums, temp)#dont add
            temp.append(nums[i])
            rec(i+1, nums, temp)
            temp.pop()

        rec(0,nums, [])
        
        return res