# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        rmin, rmax = arrays[0][0], arrays[0][-1]
        dist = 0
        for i in range(1, len(arrays)):
            dist = max(dist, abs(arrays[i][0]-rmax), abs(arrays[i][-1]-rmin))
            rmin = min(rmin, arrays[i][0])
            rmax = max(rmax, arrays[i][-1])
        return dist