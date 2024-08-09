# Problem: Magic Squares In Grid - https://leetcode.com/problems/magic-squares-in-grid/

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        squares = 0
        rows, cols = len(grid), len(grid[0]) 
        for r in range(2, rows):
            for c in range(2, cols):
                magic = True
                rig_diag = grid[r-2][c] + grid[r-1][c-1] + grid[r][c-2]
                left_diag = grid[r-2][c-2] + grid[r-1][c-1] + grid[r][c]
                if rig_diag != left_diag:
                    continue
                unique = set()
                for i in range(r-2, r+1):
                    cur = 0
                    for j in range(c-2, c+1):
                        if grid[i][j] == 0 or grid[i][j] > 9 or grid[i][j] in unique:
                            magic = False
                            break
                        cur += grid[i][j] 
                        unique.add(grid[i][j])
                    if cur != rig_diag:
                        magic = False
                        break
            
                for j in range(c-2, c+1):
                    cur = 0
                    for i in range(r-2, r+1):
                        cur += grid[i][j]
                    if cur != rig_diag:
                            magic = False
                            break        
                
                if magic:
                    squares += 1
        return squares