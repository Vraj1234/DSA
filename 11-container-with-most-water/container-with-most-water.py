class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)-1
        l,r = 0, n
        max_area = 0

        def area(l,r):
            b = r-l
            h = min(height[l], height[r])
            return b*h

        while l<r:
            max_area = max(max_area, area(l,r))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        
        return max_area
