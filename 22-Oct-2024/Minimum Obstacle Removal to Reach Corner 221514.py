# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        queue = [(0,0,0)] # number of obstacles, r, c
        visited = set()
        nbrs = [(0,1),(1,0),(-1,0),(0,-1)]
        m, n = len(grid), len(grid[0])
        while queue:
            obs, cur_r, cur_c = heappop(queue)
            if (cur_r, cur_c) == (m-1, n-1):
                return obs
            if (cur_r, cur_c) in visited:
                continue
            visited.add((cur_r, cur_c))
            for nbr_r, nbr_c in nbrs:
                nbr_r += cur_r
                nbr_c += cur_c
                if 0 <= nbr_r < m and 0 <= nbr_c < n and (nbr_r, nbr_c) not in visited:
                    heappush(queue, ((obs + 1 if grid[nbr_r][nbr_c] else obs, nbr_r, nbr_c)))
