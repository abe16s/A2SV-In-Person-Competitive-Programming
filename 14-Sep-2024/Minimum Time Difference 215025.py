# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        timePoints.append(timePoints[0])
        min_minute = float("inf")
        for i in range(1, len(timePoints)):
            hour, minute = timePoints[i].split(":")
            prev_h, prev_m = timePoints[i-1].split(":")
            cur = (int(hour) - int(prev_h))*60 - int(prev_m) + int(minute)
            if i == len(timePoints)-1:
                cur *= -1
            min_minute = min(min_minute, cur, abs(cur-1440))

        return min_minute