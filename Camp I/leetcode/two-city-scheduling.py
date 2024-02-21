class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1]-x[0])
        total = 0
        for i in range(len(costs)//2):
            total += costs[i][1]
            total += costs[len(costs)-1-i][0]
        return total