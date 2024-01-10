class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dic = {}
        maxi = float("inf")
        for i in range(len(cards)):
            if cards[i] in dic:
                maxi = min(maxi, i - dic[cards[i]]+1)
            
            dic[cards[i]] = i

        return maxi if maxi != float("inf") else -1