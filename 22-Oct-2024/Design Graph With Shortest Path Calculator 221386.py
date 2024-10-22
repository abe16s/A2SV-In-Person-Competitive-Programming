# Problem: Design Graph With Shortest Path Calculator - https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        for f, t, c in edges:
            self.graph[f].append((t, c))

    def addEdge(self, edge: List[int]) -> None:
        f, t, c = edge
        self.graph[f].append((t, c))

    def shortestPath(self, node1: int, node2: int) -> int:
        queue = [(0, node1)]
        visited = set()
        while queue:
            cur_cost, cur_node = heappop(queue)
            if cur_node == node2:
                return cur_cost
            visited.add(cur_node)
            for nbr, nbr_cost in self.graph[cur_node]:
                if nbr not in visited:
                    heappush(queue, (cur_cost+nbr_cost, nbr))
        return -1
            



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)