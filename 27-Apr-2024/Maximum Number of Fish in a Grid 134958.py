# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                if rank[parentX] > rank[parentY]:
                    parent[parentY] = parentX
                    p, c = parentX, parentY
                elif rank[parentX] < rank[parentY]:
                    parent[parentX] = parentY
                    p, c = parentY, parentX
                else:
                    parent[parentX] = parentY
                    rank[parentY] += 1
                    p, c = parentY, parentX
                fishes[p] += fishes[c]
        
        m = len(grid)
        n = len(grid[0])
        parent = {}
        fishes = {}
        rank = defaultdict(int)
        for i in range(m):
            for j in range(n):
                parent[(i,j)] = (i,j)
                fishes[(i,j)] = grid[i][j]

        nbrs = [(0,1), (1,0), (-1,0), (0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for dx, dy in nbrs:
                        nbr_r = i + dx
                        nbr_c = j + dy
                        if 0 <= nbr_r < m and 0 <= nbr_c < n and grid[nbr_r][nbr_c] > 0:
                            union((i,j), (nbr_r, nbr_c))
        return max(fishes.values())