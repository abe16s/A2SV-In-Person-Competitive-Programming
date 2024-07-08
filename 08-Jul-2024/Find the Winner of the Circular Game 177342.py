# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1,n+1)]
        current = 0
        while len(players) > 1:
            start = current
            for i in range(k-1):
                current += 1
            current %= len(players)
            players.pop(current)
        return players[0]