# Problem: Distinct Subsequences - https://leetcode.com/problems/distinct-subsequences/description/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        dp = [[0]*m for _ in range(n)]
        for i in range(m):
            if s[i] == t[0]:
                dp[0][i] += 1
            if i > 0:
                dp[0][i] += dp[0][i-1]
        for i in range(1, n):
            for j in range(i, m):
                if s[j] == t[i]:
                    dp[i][j] += dp[i-1][j-1]
                dp[i][j] += dp[i][j-1] 

        return dp[n-1][m-1]