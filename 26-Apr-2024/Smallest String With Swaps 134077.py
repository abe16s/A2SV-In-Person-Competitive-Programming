# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
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

        n = len(s)
        parent = [i for i in range(n)]
        rank = [1] * n
        for a, b in pairs:
            union(a,b)
        
        equals = defaultdict(list)
        for p in range(n):
            equals[find(p)].append(s[p])

        for k in equals:
            equals[k].sort(reverse=True)
        
        cout = ""
        for i in range(n):
            cout += equals[find(i)].pop()
        
        return cout