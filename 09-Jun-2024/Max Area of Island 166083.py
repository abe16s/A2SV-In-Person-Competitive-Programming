# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        color = []

        for r in range(len(grid)):
            color.append([])
            for c in range(len(grid[0])):
                color[r].append(0)
                
        def dfs(index, prev):
            r, c = index
            neighbours = [(r-1,c), (r+1,c), (r,c-1),(r,c+1)]
            color[r][c] = 1
            cur_area = 0
            for nbr_r, nbr_c in neighbours:
                if 0 <= nbr_r < len(grid) and 0 <= nbr_c < len(grid[0]):
                    if grid[nbr_r][nbr_c] == 1 and color[nbr_r][nbr_c] == 0:
                        cur_area += dfs((nbr_r, nbr_c), index)
            return cur_area + 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if color[r][c] == 0 and grid[r][c] == 1:
                    area = dfs((r,c), (-1,-1))
                    max_area = max(max_area, area)
        
        return max_area

        