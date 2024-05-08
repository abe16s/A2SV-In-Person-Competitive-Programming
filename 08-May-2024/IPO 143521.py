# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cap_idx = [[capital[idx], profits[idx]] for idx in range(len(capital))]
        cap_idx.sort()
        maxHeap = []
        i = 0
        for _ in range(k):
            while i < len(capital) and cap_idx[i][0] <= w:
                heappush(maxHeap, -cap_idx[i][1])
                i += 1
            if not maxHeap:
                break
            w -= heappop(maxHeap)

        return w