class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        t = temperatures
        res = [0]*n
        stack = []
        stack.append((t[0], 0))
        for i in range(1,n):
            while stack and t[i]>stack[-1][0]:
                top_num = stack[-1][0]
                top_idx = stack[-1][1]
                res[top_idx] = i-top_idx
                stack.pop()
            stack.append((t[i], i))
        return res