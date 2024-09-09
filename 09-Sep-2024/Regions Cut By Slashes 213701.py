# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def find(x):
            if not parent[x]:
                parent[x] = x
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
                elif rank[parentX] < rank[parentY]:
                    parent[parentX] = parentY
                else:
                    parent[parentX] = parentY
                    rank[parentY] += 1
        
        parent = defaultdict(tuple)
        rank = defaultdict(int)

        n = len(grid)
        for i in range(n):
            for j in range(n):
                if i:
                    union((i-1, j, 2), (i, j, 0))
                if j:
                    union((i, j-1, 1), (i, j, 3))
                if grid[i][j] != "/":
                    union((i,j,0), (i,j,1))
                    union((i,j,2), (i,j,3))
                if grid[i][j] != "\\":
                    union((i,j,0), (i,j,3))
                    union((i,j,2), (i,j,1))

        return len(set(map(find, parent)))