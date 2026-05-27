class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        ready = [] #(-freq, key)
        cooldown = [] #(available, key)
        res = []

        for key, freq in c.items():
            heapq.heappush(ready, (-freq, key))
        
        cur = 0
        while c:
            while cooldown and cooldown[0][0] <= cur:
                available, key = heapq.heappop(cooldown)
                heapq.heappush(ready, (-c[key], key))
            if ready:
                _, key = heapq.heappop(ready)
                res.append(key)
                c[key]-=1
                if c[key] == 0:
                    del c[key]
                else:
                    available = cur + n + 1
                    heapq.heappush(cooldown, (available, key))
            else:
                res.append("idle")
            cur+=1
        
        return len(res)
            
