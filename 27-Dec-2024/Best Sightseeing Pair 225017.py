# Problem: Best Sightseeing Pair - https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxi = values[0]
        max_score = 0
        for j in range(1, len(values)):
            max_score = max(max_score, values[j]-j+maxi)
            maxi = max(maxi, values[j]+j)
        return max_score