# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
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

        parent = {s:s for s in strs}
        rank = defaultdict(int)
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                ctr = 0
                for k in range(len(strs[0])):
                    if strs[i][k] != strs[j][k]:
                        ctr += 1
                if ctr <= 2:
                    union(strs[i], strs[j])
        
        roots = set()
        for s in strs:
            roots.add(find(s))
        
        return len(roots)