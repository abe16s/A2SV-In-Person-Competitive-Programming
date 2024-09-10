# Problem: Number of Closed Islands - https://leetcode.com/problems/number-of-closed-islands/

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def dfs(r, c):
            nbrs = [(1,0), (0,1), (-1,0), (0,-1)]
            closed = True
            grid[r][c] = 1
            for nbr_r, nbr_c in nbrs:
                nbr_r += r
                nbr_c += c
                if not(0<=nbr_r<n and 0<=nbr_c<m):
                    closed = False
                    continue
                if grid[nbr_r][nbr_c] == 0: 
                    closed = dfs(nbr_r, nbr_c) and closed
            return closed
        
        ctr = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0 and dfs(r, c):
                    ctr += 1
        return ctr