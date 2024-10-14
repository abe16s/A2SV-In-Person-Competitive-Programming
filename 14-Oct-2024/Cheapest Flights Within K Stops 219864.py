# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float("inf")] * n
        dp[src] = 0

        for i in range(k+1):
            cur = dp[:]
            any_relaxation = False
            for f, t, w in flights: 
                if dp[f] != float('inf') and dp[t] > cur[f] + w:
                    dp[t] =cur[f] + w
                    any_relaxation = True

            if not any_relaxation:
                break

        return dp[dst] if dp[dst] != float("inf") else -1