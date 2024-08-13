# Problem: Total Cost to Hire K Workers - https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        first = []
        last = []
        i, j = 0, len(costs)-1
        while i <= j and i < candidates:
            if i == j:
                heapq.heappush(first, costs[i])
                i += 1
                break
            heapq.heappush(first, costs[i])
            heapq.heappush(last, costs[j])
            i += 1
            j -= 1
        cost = 0
        for l in range(k):
            if not last or (first and first[0] <= last[0]):
                cost += heapq.heappop(first)
                if i <= j:
                    heapq.heappush(first, costs[i])
                    i += 1
            else:
                cost += heapq.heappop(last)
                if j >= i:
                    heapq.heappush(last, costs[j])
                    j -= 1

        return cost
