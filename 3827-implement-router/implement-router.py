class Router:

    def __init__(self, memoryLimit: int):
        self.q = deque()
        self.seen = set()
        self.map = defaultdict(deque)
        self.limit = memoryLimit

    def remove_packet(self):
        s,d,t = self.q.popleft()
        self.seen.remove((s,d,t))
        self.map[d].popleft()
        if len(self.map[d])==0:
            del self.map[d]
        
        return [s,d,t]

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.seen:
            
            return False
        elif len(self.q) == self.limit:
            self.remove_packet()
            
        self.q.append(packet)
        self.seen.add(packet)
        self.map[destination].append(timestamp)
        
        return True
    

    def forwardPacket(self) -> List[int]:
        if self.q:
            return self.remove_packet()
        else:
            
            return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ts = self.map[destination]
        l_index = bisect.bisect_left(ts, startTime)
        r_index = bisect.bisect_right(ts, endTime)
        # print(ts, l_index, r_index, startTime, endTime)
        return r_index-l_index

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)