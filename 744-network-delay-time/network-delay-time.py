class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s,d,t in times:
            adj[s].append((d,t))
        
        times = [float('inf')] * (n+1)
        times[k] = 0
        vis = set()
        heap = []
        heapq.heappush(heap, (0,k))
        while heap:
            cur_t, node = heapq.heappop(heap)
            if node in vis:
                continue
            vis.add(node)
            for neighbor, t in adj[node]:
                if neighbor not in vis and cur_t+t < times[neighbor]:
                    times[neighbor] = cur_t + t
                    heapq.heappush(heap, (cur_t+t, neighbor))
        
        res = max(times[1:])
        return -1 if res == float('inf') else res
            
