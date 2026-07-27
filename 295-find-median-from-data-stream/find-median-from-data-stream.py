class MedianFinder:

    def __init__(self):
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:
        if (not self.left_max and not self.right_min):
            heapq.heappush(self.left_max, -1 * num)
            return
        if len(self.left_max) == len(self.right_min):
            if num>= -1* self.left_max[0]:
                heapq.heappush(self.right_min, num)
            else:
                heapq.heappush(self.right_min, -1 * heapq.heappop(self.left_max))
                heapq.heappush(self.left_max, -1 * num)
        elif len(self.left_max) > len(self.right_min):
            if num>= -1 * self.left_max[0]:
                heapq.heappush(self.right_min, num)
            else:
                heapq.heappush(self.right_min, -1 * heapq.heappop(self.left_max))
                heapq.heappush(self.left_max, -1 * num)
        else:
            if num<=self.right_min[0]:
                heapq.heappush(self.left_max, -1 * num)
            else:
                heapq.heappush(self.left_max, -1 * heapq.heappop(self.right_min))
                heapq.heappush(self.right_min, num)


    def findMedian(self) -> float:
        if len(self.left_max) == len(self.right_min):
            print(-1* self.left_max[0], self.right_min[0])
            return (-1* self.left_max[0] + self.right_min[0])/2
        
        if len(self.left_max) > len(self.right_min):
            return -1* self.left_max[0]
        else:
            return self.right_min[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()