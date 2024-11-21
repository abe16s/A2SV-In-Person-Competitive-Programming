# Problem: Longest Path With Different Adjacent Characters - https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.parent = parent
        self.s = s
        self.tree = defaultdict(list)
        self.longest = 0
        for i in range(1, len(self.parent)):
            self.tree[self.parent[i]].append(i)

        self.dfs(0)
        return self.longest

    def dfs(self, node):
        a = b = 0
        for child in self.tree[node]:
            cur = self.dfs(child)
            if cur >= b:
                a, b = b, cur
            elif cur >= a:
                a = cur
        
        self.longest = max(self.longest, a + b + 1)
        if node != 0 and self.s[self.parent[node]] == self.s[node]:
            return 0
        return b + 1
