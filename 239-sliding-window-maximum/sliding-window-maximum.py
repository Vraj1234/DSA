class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k>=len(nums):
            return [max(nums)]

        q = deque()
        res = []
        l = r = 0
        n = len(nums)
        while r<k:
            while q and nums[r]> nums[q[-1]]:
                q.pop()
            q.append(r)
            r+=1
        
        res.append(nums[q[0]])
        print(q)
        while r<n:

            if l == q[0]:
                q.popleft()
            l+=1
            while q and nums[r]> nums[q[-1]]:
                q.pop()
            q.append(r)
            r+=1
            res.append(nums[q[0]])
        
        return res