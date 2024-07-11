# Problem: Minimum Height Trees  - https://leetcode.com/problems/minimum-height-trees/description/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(set)
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)
        
        queue = deque()
        for i in range(n):
            if len(tree[i]) == 1:
                queue.append(i)
        
        cout = [0]
        while queue:
            cout = queue.copy()
            for i in range(len(queue)):
                cur = queue.popleft()
                for nbr in tree[cur]:
                    tree[nbr].remove(cur)
                    if len(tree[nbr]) == 1:
                        queue.append(nbr)
                tree.pop(cur)
        return cout


