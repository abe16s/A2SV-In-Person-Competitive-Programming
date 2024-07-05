# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            j = 1
            while i - j*j >= 0:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[-1]