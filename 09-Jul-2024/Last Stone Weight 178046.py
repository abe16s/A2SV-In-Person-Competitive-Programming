# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for s in stones:
            heapq.heappush(maxHeap, -s)
        while len(maxHeap) > 1:
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)

            if stone1 != stone2:
                heapq.heappush(maxHeap, -abs(stone1-stone2))
        return -sum(maxHeap)
