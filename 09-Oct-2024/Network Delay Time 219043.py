# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        mini = float("inf")
        heap = [(0, k)]
        processed = set()
        while heap:
            dist, cur = heapq.heappop(heap)
            if cur in processed:
                continue
            mini = dist
            processed.add(cur)
            for nbr, nbr_dist in graph[cur]:
                if nbr not in processed:
                    heapq.heappush(heap, (dist+nbr_dist, nbr))

        return mini if len(processed) == n else -1 