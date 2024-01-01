class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = len(piles) // 3
        j = len(piles) - 2
        total = 0 
        while i > 0:
            total += piles[j]
            j -= 2
            i -= 1
        return total

            