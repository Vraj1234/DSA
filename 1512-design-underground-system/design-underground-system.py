class UndergroundSystem:

    def __init__(self):
        self.by_id = {}
        self.travel_times = {}
    
    def avg(self, l):
        return sum(l)/len(l)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.by_id[id] = (stationName, int(t))
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        stn, minutes = self.by_id[id]
        travel_times_key = stn + "&" + stationName
        if travel_times_key not in self.travel_times:
            self.travel_times[travel_times_key] = []
        self.travel_times[travel_times_key].append(int(t)- int(minutes))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg(self.travel_times[startStation + "&" + endStation])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)