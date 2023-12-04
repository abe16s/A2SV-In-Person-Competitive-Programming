class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def fun(pt1, pt2):
            time = 0
            if abs(pt1[0]-pt2[0]) < abs(pt1[1]-pt2[1]):
                time = abs(pt2[0]-pt1[0])
                if pt1[1] > pt2[1]:
                    pt1[1] -= time
                    time += (pt1[1]-pt2[1])
                else:
                    pt1[1] += time
                    time += (pt2[1]-pt1[1])
            else:
                time = abs(pt2[1]-pt1[1])
                if pt1[0] > pt2[0]:
                    pt1[0] -= time 
                    time += (pt1[0]-pt2[0])
                else:
                    pt1[0] += time
                    time += (pt2[0]-pt1[0])
            return time
        total = 0
        for i in range(len(points)-1):
            total += fun(points[i],points[i+1])
        return total
