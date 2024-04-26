# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        nbrs = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r,c):
            cout = True
            if grid1[r][c] == 0:
                cout = False
                
            grid2[r][c] = 2
            
            for dx, dy in nbrs:
                nbr_r = r + dx
                nbr_c = c + dy
                if 0 <= nbr_r < m  and 0 <= nbr_c < n and grid2[nbr_r][nbr_c] == 1:
                    if dfs(nbr_r, nbr_c) == False:
                        cout = False
            return cout

        ctr = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i,j):
                        ctr += 1
        return ctr

