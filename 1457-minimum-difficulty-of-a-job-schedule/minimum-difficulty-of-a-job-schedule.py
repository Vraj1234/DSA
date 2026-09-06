class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        
        dp = {}

        def f(i, d, cur_max):
            if d == 0:
                if i == n:
                    return 0
                else:
                    return float('inf')
            
            if i >= n:
                return float('inf')
            
            if dp.get((i,d,cur_max), -1) != -1:
                return dp[(i,d,cur_max)]

            cur_max = max(cur_max, jobDifficulty[i])

            end_day = cur_max + f(i+1, d-1, -1)
            dont_end_day = f(i+1, d, cur_max)

            dp[(i,d,cur_max)] = min(end_day, dont_end_day)
            return min(end_day, dont_end_day)

        return f(0,d,-1)