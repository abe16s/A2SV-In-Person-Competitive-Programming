class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = [0] * (max(costs)+1)
        for c in costs:
            count[c] += 1
        k = 0
        for c in range(len(count)):            
            while count[c]:
                costs[k] = c
                count[c] -= 1
                k += 1
        total = 0
        i = 0
        while i<len(costs) and total <= coins:
            total += costs[i]
            i+=1
            if total > coins:
                return i-1
        return i