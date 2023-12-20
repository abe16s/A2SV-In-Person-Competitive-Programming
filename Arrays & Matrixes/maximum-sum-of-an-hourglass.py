class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        hourglass = 0
        for r in range(1, len(grid)-1):
            for c in range(1,len(grid[0])-1):
                total = grid[r][c]
                total += grid[r-1][c-1]
                total += grid[r-1][c]
                total += grid[r-1][c+1]
                total += grid[r+1][c-1]
                total += grid[r+1][c]
                total += grid[r+1][c+1]
                hourglass = max(total, hourglass)
        return hourglass 