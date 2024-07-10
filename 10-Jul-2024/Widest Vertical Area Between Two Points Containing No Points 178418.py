# Problem: Widest Vertical Area Between Two Points Containing No Points - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        maxi = 0
        for i in range(1,len(points)):
            maxi = max(maxi, points[i][0]-points[i-1][0])
        return maxi