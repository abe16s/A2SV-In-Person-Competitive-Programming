# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def change(_sum, idx):
            if _sum > amount or idx >= len(coins):
                return 0
            if _sum == amount:
                return 1

            if (_sum, idx) not in memo:
                picked = change(_sum+coins[idx], idx)
                nonpicked = change(_sum, idx+1)
                memo[(_sum, idx)] = picked + nonpicked

            return memo[(_sum, idx)]
        
        return change(0, 0)