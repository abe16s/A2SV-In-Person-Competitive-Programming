# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for p in prices:
            profit = max(profit, p-buy)
            buy = min(p, buy)
        return profit
