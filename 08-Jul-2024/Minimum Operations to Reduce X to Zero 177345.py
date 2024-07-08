# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        l = 0
        wind = 0
        n = len(nums)
        mini = float("inf")
        for r in range(n):
            wind += nums[r]
            while l<=r and wind > target:
                wind -= nums[l]
                l += 1
            if wind == target:
                mini = min(mini, n-(r-l+1))
        return -1 if mini == float("inf") else mini