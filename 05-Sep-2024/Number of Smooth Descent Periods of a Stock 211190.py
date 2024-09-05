# Problem: Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        smooth = 0
        s = 0
        n = len(prices)
        while s < n:
            f = s+1
            while f < len(prices) and prices[f-1]-prices[f] == 1:
                f += 1
            x = f-s
            smooth += x*(x+1)//2
            s = f

        return smooth