# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        for f, t, w in edges:
            graph[f].append([t,w])
            graph[t].append([f,w])

        def shortest(node, graph, distanceThreshold):
            queue = [[0, node]]
            reachable = 0
            visited = set()
            
            while queue:
                dist, cur = heapq.heappop(queue)
                if cur in visited:
                    continue
                visited.add(cur)
                reachable += 1
                for nbr in graph[cur]:
                    if nbr[0] not in visited and dist + nbr[1] <= distanceThreshold:
                        heapq.heappush(queue, [dist + nbr[1], nbr[0]])
            return reachable

        smallest = n + 1
        ans = 0
        for i in range(n):
            cur = shortest(i, graph, distanceThreshold)
            if cur <= smallest:
                ans = i
                smallest = cur
        return ans