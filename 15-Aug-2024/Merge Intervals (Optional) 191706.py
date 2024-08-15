# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        cout = []
        i = 0
        while i < len(intervals):
            curr = [intervals[i][0]]
            maxi = intervals[i][-1] 
            i += 1
            while i < len(intervals) and maxi >= intervals[i][0]:
                maxi = max(maxi, intervals[i][-1])
                i += 1 
            curr.append(maxi)
            cout.append(curr)
        return cout