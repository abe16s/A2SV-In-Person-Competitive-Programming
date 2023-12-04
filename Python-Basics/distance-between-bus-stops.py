class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        dir1 = 0
        dir2 = 0
        n = len(distance)
        i = start
        while i != destination:
            dir1 += distance[i]
            i = (i+1) % n
        j = destination
        while j != start:
            dir2 += distance[j]
            j = (j+1) % n
        return min(dir1,dir2)
