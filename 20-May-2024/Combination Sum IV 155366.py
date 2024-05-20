# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(idx, cur_sum):
            if cur_sum > target or idx == len(nums):
                return 0
            if cur_sum == target:
                return 1

            if (idx, cur_sum) not in memo:
                cur = 0
                for i in range(len(nums)):
                    cur += dp(i, cur_sum+nums[i])
                memo[(idx, cur_sum)] = cur
            return memo[(idx, cur_sum)]

        return dp(0, 0)     
