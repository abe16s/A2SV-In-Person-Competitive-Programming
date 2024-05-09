# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        ans = 0
        pairs = list(zip(efficiency, speed))
        pairs.sort(reverse=True)
        heap = []
        total = 0
        for e, s in pairs:
            heappush(heap, s)
            total += s
            if len(heap) > k:
                total -= heappop(heap)
            ans = max(ans, total*e)

        return ans % (10**9+7)