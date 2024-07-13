# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ctr = 0
        i = 0 
        while i < len(prices):
            while i+1 < len(prices) and prices[i+1] <= prices[i]:
                i += 1 
            buy = i
            while i+1 < len(prices) and prices[i+1] >= prices[i]:
                i += 1
            sell = i
            ctr += (prices[sell]-prices[buy])
            i += 1
        return ctr