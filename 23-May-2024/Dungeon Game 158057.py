# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0]*n for _ in range(m)]
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if (r,c) == (m-1,n-1):
                    dp[m-1][n-1] = 1 if dungeon[-1][-1] > 0 else 1 - dungeon[-1][-1]
                    continue
                cur = float("inf")
                if r+1 < m:
                    cur = min(cur, dp[r+1][c])
                if c+1 < n:
                    cur = min(cur, dp[r][c+1])
                dp[r][c] = 1 if dungeon[r][c] >= cur else cur - dungeon[r][c]
        return dp[0][0]