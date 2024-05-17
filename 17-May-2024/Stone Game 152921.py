# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)
        memo = {}
        def dp(front,rear):
            if front > rear:
                return 0

            if (front, rear) not in memo:
                take_front = piles[front] - dp(front+1, rear)
                take_rear = piles[rear] - dp(front, rear-1)
                memo[(front, rear)] = max(take_front, take_rear)

            return memo[(front, rear)]
            
        return dp(0, len(piles)-1) >= 0