# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dp(cur):
            if cur not in memo:
                res = 1
                for i in range(1,cur):
                    res = max(res, i*dp(cur-i), i*(cur-i))
                memo[cur] = res
            return memo[cur]

        return dp(n)
