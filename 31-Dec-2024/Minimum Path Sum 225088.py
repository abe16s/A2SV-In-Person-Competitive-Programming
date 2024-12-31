# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if (r,c) == (0,0):
                    continue
                grid[r][c] += min(grid[r-1][c] if r-1 >= 0 else float('inf'), grid[r][c-1] if c-1 >=0 else float('inf'))
        
        return grid[-1][-1]