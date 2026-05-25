class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        self.i = 0
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        if self.i < self.k:
            heapq.heappush(self.heap, val)
        else:
            if val > self.heap[0]:
                heapq.heappush(self.heap, val)
                heapq.heappop(self.heap)
        self.i+=1
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)