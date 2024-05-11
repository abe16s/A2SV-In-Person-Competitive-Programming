# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def change(_sum):
            if _sum > amount:
                return float("inf")
            if _sum == amount:
                return 0

            if _sum in memo:
                return memo[_sum]

            res = float("inf")
            for i in range(len(coins)):
                    res = min(res, change(_sum+coins[i])) 
            memo[_sum] = res + 1
            return res + 1

        cout = change(0)
        return  cout if cout != float("inf") else -1