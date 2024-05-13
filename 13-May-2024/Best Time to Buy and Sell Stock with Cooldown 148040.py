# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i, buy):
            if i == len(prices):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]
            if buy == 1:
                buying = dp(i+1, 2) - prices[i]
                notbuying = dp(i+1, 1)
                memo[(i,buy)] = max(buying, notbuying)
                return memo[(i,buy)]
            elif buy == 2:
                selling = dp(i+1, 3) + prices[i]
                notselling = dp(i+1, 2)
                memo[(i,buy)] = max(selling, notselling)
                return memo[(i,buy)]
            elif buy == 3:
                cooldown = dp(i+1, 1) 
                memo[(i,buy)] = cooldown
                return memo[(i, buy)]
                
        return dp(0, 1)