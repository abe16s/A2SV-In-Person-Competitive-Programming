# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        disconnected = 0
        unreachable = 0
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def bfs(node):
            queue = deque([node])
            nodes = 0
            while queue:
                cur = queue.popleft()
                nodes += 1
                for nbr in graph[cur]:
                    if nbr not in visited:
                        queue.append(nbr)
                        visited.add(nbr)
            return nodes

        for i in range(n):
            if i not in visited:
                visited.add(i)
                search = bfs(i)
                unreachable += disconnected * search
                disconnected += search

        return unreachable
