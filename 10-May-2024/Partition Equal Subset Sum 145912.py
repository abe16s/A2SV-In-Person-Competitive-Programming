# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        memo = {}
        def sm(n, _sum):
            if n >= len(nums):
                return False
            if _sum == total//2:
                return True
            if (n, _sum) in memo:
                return memo[(n, _sum)]
            res = sm(n+1, _sum+nums[n]) or sm(n+1, _sum)
            memo[(n, _sum)] = res
            return res

        sm(0,0)
        return memo[(0,0)]
