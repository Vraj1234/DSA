class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_sum = []
        s_sum = []
        mx = height[0]

        for x in height:
            mx = x if x > mx else mx
            prefix_sum.append(mx)
        
        mx = height[-1]
        for x in height[::-1]:
            mx = x if x > mx else mx
            s_sum.append(mx)

        suffix_sum = s_sum[::-1]
        
        res = 0
        for i,x in enumerate(height):
            if x<prefix_sum[i] and x<suffix_sum[i]:
                res+= min(prefix_sum[i], suffix_sum[i]) - x
        
        return res

        