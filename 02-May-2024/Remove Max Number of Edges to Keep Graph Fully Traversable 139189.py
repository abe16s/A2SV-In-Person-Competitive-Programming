# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class Union():
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parentX = self.find(x)
        self.parentY = self.find(y)
        if self.parentX != self.parentY:
            if self.rank[self.parentX] > self.rank[self.parentY]:
                self.parent[self.parentY] = self.parentX
            elif self.rank[self.parentX] < self.rank[self.parentY]:
                self.parent[self.parentX] = self.parentY
            else:
                self.parent[self.parentX] = self.parentY
                self.rank[self.parentY] += 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse=True)
        alice = Union(n)
        bob = Union(n)
        removed = 0
        for t, u, v in edges:
            if t == 3:
                if alice.find(u-1) == alice.find(v-1) and bob.find(u-1) == bob.find(v-1):
                    removed += 1
                else:
                    alice.union(u-1,v-1)
                    bob.union(u-1, v-1)
            elif t == 1:
                if alice.find(u-1) == alice.find(v-1):
                    removed += 1
                else:
                    alice.union(u-1, v-1)
            else:
                if bob.find(u-1) == bob.find(v-1):
                    removed += 1
                else:
                    bob.union(u-1, v-1)

        for i in range(n-1):
            if alice.find(i) != alice.find(i+1) or bob.find(i) != bob.find(i+1):
                return -1

        return removed