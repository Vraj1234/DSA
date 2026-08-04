class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize != 0:
            return False

        c = Counter(hand)
        heap = []
        for key, value in c.items():
            heapq.heappush(heap, (key))
        
        while heap:
            
            num = heap[0]
            for i in range(groupSize):
                if num+i in c:
                    c[num+i]-=1
                    if c[num+i] ==0:
                        del c[num+i]
                        heapq.heappop(heap)
                else:
                    return False
        
        return True


        