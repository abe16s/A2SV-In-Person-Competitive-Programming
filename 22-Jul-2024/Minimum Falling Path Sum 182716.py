# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[n-1][i] = matrix[n-1][i]
        
        for r in range(n-2,-1,-1):
            for c in range(n):
                cur = float("inf")
                for nbr in range(3):
                    if 0 <= c+nbr-1 < n:
                        cur = min(cur, dp[r+1][c+nbr-1])
                dp[r][c] = cur + matrix[r][c]

        return min(dp[0])