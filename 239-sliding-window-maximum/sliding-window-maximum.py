class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        l,r = 0, 0
        q = deque()
        while r<k:
            while q and nums[r]>=nums[q[-1]]:
                q.pop()
            q.append(r)
            r+=1
        r-=1
        res = []
        res.append(nums[q[0]])
        while r<n:
            if l == q[0]:
                q.popleft()
            l+=1
            r+=1
            if r<n:
                while q and nums[r]>=nums[q[-1]]:
                    q.pop()
                q.append(r)
                res.append(nums[q[0]])
        
        return res
