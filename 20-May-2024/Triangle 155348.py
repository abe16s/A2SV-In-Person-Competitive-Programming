# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[] for _ in range(len(triangle))]
        dp[0].append(triangle[0][0])
        for r in range(1,len(triangle)):
            for c in range(r+1):
                cur = float("inf")
                if  0 <= c-1 < r:
                    cur = min(cur, dp[r-1][c-1])
                if 0 <= c < r:
                    cur = min(cur, dp[r-1][c])
                dp[r].append(cur+triangle[r][c])
        
        return min(dp[-1])
