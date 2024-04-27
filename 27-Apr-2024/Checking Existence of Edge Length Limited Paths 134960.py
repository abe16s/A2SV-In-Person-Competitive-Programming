# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        for q in range(len(queries)):
            queries[q].append(q)
        queries.sort(key=lambda x: x[2])
        
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
        
        parent = [i for i in range(n)]
        rank = [1] * n
        e = 0
        cout = [False]*len(queries)
        for q in range(len(queries)):
            a, b, c, d = queries[q]
            while e < len(edgeList) and edgeList[e][2] < c:
                x,y,z = edgeList[e]
                union(x,y)
                e += 1
            cout[d] = find(a) == find(b)

        return cout

