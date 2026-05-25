class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        i = 0
        for point in points:
            x,y = point
            dist = sqrt(x*x + y*y)
            if i < k:   
                heapq.heappush(heap, (-dist, point))
            else:
                if dist < -heap[0][0]:
                    heapq.heappush(heap, (-dist, point))
                    heapq.heappop(heap)
            i+=1

        res = [e[1] for e in heap]
        return res

        