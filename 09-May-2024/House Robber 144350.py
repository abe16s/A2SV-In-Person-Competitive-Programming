# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def robber(n):
            if n >= len(nums):
                return 0
            if n not in memo:
                memo[n] = max(robber(n+2), robber(n+3)) + nums[n]
            return memo[n]

        return max(robber(0), robber(1))