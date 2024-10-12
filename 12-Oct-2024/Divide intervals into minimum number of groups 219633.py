# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        ps = [0] * (1000001)
        for l, r in intervals:
            ps[l-1] += 1
            ps[r] -= 1
        
        mini = 1
        for i in range(1, len(ps)):
            ps[i] += ps[i-1]
            mini = max(mini, ps[i])
        
        return mini