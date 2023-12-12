class UndergroundSystem:
    def __init__(self):
        self.checkins = {}
        self.travels_sum = defaultdict(int)
        self.travels_customers = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = [t, stationName]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time = t - self.checkins[id][0]
        self.travels_sum[self.checkins[id][1]+"$"+stationName] += time
        self.travels_customers[self.checkins[id][1]+"$"+stationName] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.travels_sum[startStation+"$"+endStation] / self.travels_customers[startStation+"$"+endStation]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)