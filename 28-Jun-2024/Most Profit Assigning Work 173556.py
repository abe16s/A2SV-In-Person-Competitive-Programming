# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        work = [[difficulty[i], profit[i]] for i in range(len(difficulty))]
        work.sort()
        worker.sort()
        maxProfit = 0
        w = 0
        profit = 0
        for r in range(len(worker)):
            while w < len(work) and work[w][0] <= worker[r]:
                maxProfit = max(maxProfit, work[w][1])
                w += 1
            profit += maxProfit
            
        return profit