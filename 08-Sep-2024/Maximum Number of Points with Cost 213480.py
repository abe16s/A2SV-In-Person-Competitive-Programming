# Problem: Maximum Number of Points with Cost - https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = [[0] * n for _ in range(m)]
        dp[m-1] = points[m-1]
        for r in range(m-2, -1, -1):
            lft = [dp[r+1][0]] 
            rgt = [0] * n
            rgt[-1] = dp[r+1][-1]
            for i in range(1,n):
                lft.append(max(lft[-1]-1,dp[r+1][i]))
                rgt[n-1-i] = max(rgt[n-i]-1, dp[r+1][n-i-1])
            for c in range(n):
                dp[r][c] = points[r][c] + max(lft[c], rgt[c])
        return max(dp[0])