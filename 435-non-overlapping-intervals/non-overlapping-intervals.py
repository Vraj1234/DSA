class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        intervals.sort(key = lambda x:x[1])
        res = 0
        cur = -5 * 10**4
        for start, end in intervals:
            if cur<=start:
                res+=1
                cur = end
        
        return len(intervals)-res