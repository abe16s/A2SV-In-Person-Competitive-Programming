# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(idx, buy, transactions):
            if idx >= len(prices) or transactions >= 2:
                return 0
            if (idx, buy, transactions) not in memo:
                if buy:
                    buying = dp(idx+1, False, transactions)-prices[idx]
                    notbuying = dp(idx+1, True, transactions)
                    memo[(idx, buy, transactions)] = max(buying, notbuying)
                else:
                    selling = dp(idx+1, True, transactions+1) + prices[idx]
                    notselling = dp(idx+1, False, transactions) 
                    memo[(idx, buy, transactions)] = max(selling, notselling)
            
            return memo[(idx, buy, transactions)]
        
        return dp(0, True, 0)
