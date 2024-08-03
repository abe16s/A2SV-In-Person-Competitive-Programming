# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def factors(self, n):
        fact = []
        for f in range(1,n//2+1):
            if n % f == 0:
                fact.append(f)
        return fact

    def minSteps(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        dp[1] = 0
        fact = self.factors(n)
        for f in fact:
            if dp[f] == float("inf"):
                dp[f] = self.minSteps(f)
            dp[n] = min(dp[n], dp[f]+n//f)
        return dp[n]