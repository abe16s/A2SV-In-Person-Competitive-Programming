# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y, c):
            parentX = find(x)
            parentY = find(y)
            if parentX != parentY:
                if rank[parentX] > rank[parentY]:
                    parent[parentY] = parentX
                    cost[parentX] |= cost[parentY] | {c}
                elif rank[parentX] < rank[parentY]:
                    parent[parentX] = parentY
                    cost[parentY] |= cost[parentX] | {c}
                else:
                    parent[parentX] = parentY
                    cost[parentY] |= cost[parentX] | {c}
                    rank[parentY] += 1
            else:
                cost[parentY] |= {c}


        parent = [i for i in range(n)]
        rank = [1] * n
        cost = defaultdict(set)
        for a, b, dist in roads:
            union(a-1, b-1, dist)
        
        return min(cost[find(0)])
            
