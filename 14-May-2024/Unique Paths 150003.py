# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(i,j):
            if i == m-1 and j == n-1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            cur = 0
            if i + 1 < m:
                cur += dp(i+1, j)
            if j + 1 < n:
                cur += dp(i, j+1)
            memo[(i,j)] = cur
            return cur
        
        return dp(0,0)