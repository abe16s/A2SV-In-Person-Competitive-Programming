# Problem: All Ancestors of a Node in a Directed Acyclic Graph  - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegree = defaultdict(int)
        nbrs = defaultdict(set)
        for a, b in edges:
            indegree[b] += 1
            nbrs[a].add(b)
        
        cout = [set() for _ in range(n)]
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                for nbr in nbrs[cur]:
                    indegree[nbr] -= 1
                    cout[nbr] = cout[nbr] | cout[cur] | {cur}
                    if indegree[nbr] == 0:
                        queue.append(nbr)
        return [sorted(c) for c in cout]
