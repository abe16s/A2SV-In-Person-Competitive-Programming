# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows_max = [0] * n 
        cols_max = [0] * n 
        for r in range(n):
            for c in range(n):
                rows_max[r] = max(rows_max[r], grid[r][c])
                cols_max[c] = max(cols_max[c], grid[r][c])
        total = 0
        for r in range(n):
            for c in range(n):
                temp = grid[r][c]
                if grid[r][c] != rows_max[r] and grid[r][c] != cols_max[c]:
                    grid[r][c] = min(rows_max[r],cols_max[c])
                total += grid[r][c] - temp
        return total
