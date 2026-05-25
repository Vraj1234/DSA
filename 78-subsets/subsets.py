class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        temp = []
        def recur(i, nums, temp):
            if i == len(nums):
                self.res.append(temp[:])
                return
            recur(i+1, nums, temp)
            temp.append(nums[i])
            recur(i+1, nums, temp)
            temp.pop()
        
        recur(0,nums,[])
        return self.res
