# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
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

        parent = {(a,b):(a,b) for a,b in stones}
        rank = defaultdict(int)

        n = len(stones)
        for i in range(n):
            a, b = stones[i]
            for j in range(i+1, n):
                x, y = stones[j]
                if a == x or b == y:
                    union((a,b), (x,y))
        
        uniques = set()
        for k in parent:
            uniques.add(find(k))
        
        return len(stones) - len(uniques)