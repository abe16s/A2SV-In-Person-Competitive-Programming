# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            a, b = edges[i]
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])

        heap = [[0,start_node]] #log(probablility), node
        visited = set()
        while heap:
            cur_p, cur_node = heapq.heappop(heap)
            if cur_node == end_node:
                return 2**(-cur_p)
            visited.add(cur_node)
            for nbr, prob in graph[cur_node]:
                if nbr not in visited:
                    if prob != 0:
                        heapq.heappush(heap, [-(-cur_p+log(prob,2)), nbr])
        return 0.0
            

