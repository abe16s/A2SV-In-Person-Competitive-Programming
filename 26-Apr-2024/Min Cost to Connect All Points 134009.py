# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
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
                elif rank[parentX] < rank[parentY]:
                    parent[parentX] = parentY
                else:
                    parent[parentX] = parentY
                    rank[parentY] += 1

        parent = {(a,b):(a,b) for a,b in points}
        rank = defaultdict(int)

        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                a, b = points[i]
                x, y = points[j]
                heappush(edges, (abs(a-x)+abs(b-y), (a,b), (x,y)))
        
        connected = 0
        cost = 0
        while connected < n-1:
            w,u,v = heappop(edges)
            if find(u) != find(v):
                cost += w
                union(u,v)
                connected += 1
        return cost

                 