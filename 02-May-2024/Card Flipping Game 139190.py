# Problem: Card Flipping Game - https://leetcode.com/problems/card-flipping-game/description/

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        onboth = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                onboth.add(fronts[i])
        mini = 2001
        for i in range(len(fronts)):
            if fronts[i] not in onboth:
                mini = min(mini, fronts[i])
            if backs[i] not in onboth:
                mini = min(mini, backs[i]) 
        return mini if mini < 2001 else 0