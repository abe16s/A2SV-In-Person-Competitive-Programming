# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        memo = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i], memo[j]+1)
        return max(memo)
        # def dp(i,mini):
        #     if i >= len(nums):
        #         return 0

            
            
        #         cur = dp(i+1, mini)
        #         if mini == -1 or nums[mini] < nums[i]:
        #             cur = max(dp(i+1, i)+1, cur)

        #         memo[(i, mini)] = cur
        #     return memo[(i, mini)]

        # fo
        # return dp(0, -1)