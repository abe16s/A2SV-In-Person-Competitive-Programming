# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dp(i, passLeft):
            if i == len(days):
                return 0

            if (i,passLeft) in memo:
                return memo[(i,passLeft)]

            if days[i] <= passLeft:
                cur = dp(i+1, passLeft)
            else:
                cur = float("inf")
                for j in range(3):
                    if j == 0:
                        cur = min(dp(i+1, days[i] + 0) + costs[j], cur)
                    elif j == 1:
                        cur = min(dp(i+1, days[i] + 6) + costs[j], cur)
                    elif j == 2:
                        cur = min(dp(i+1, days[i] + 29) + costs[j], cur)
            memo[(i,passLeft)] = cur
            return cur

        return dp(0,0)