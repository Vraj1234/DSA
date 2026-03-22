class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = list(accumulate(height, max))
        suffix = list(accumulate(height[::-1], max))[::-1]
        count = 0
        for i,x in enumerate(height):
            count+= abs(x - min(prefix[i], suffix[i]))
        
        return count