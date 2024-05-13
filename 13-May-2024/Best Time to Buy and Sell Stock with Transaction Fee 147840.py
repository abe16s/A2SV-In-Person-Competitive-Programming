# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def dp(i, buy):
            if i == len(prices):
                return 0

            if buy:
                buying = dp(i+1, False) - prices[i] - fee
                notbuying = dp(i+1, True)
                return max(buying, notbuying)
            else:
                selling = dp(i+1, True) + prices[i]
                notselling = dp(i+1, False)
                return max(selling, notselling)

        return dp(0, True)