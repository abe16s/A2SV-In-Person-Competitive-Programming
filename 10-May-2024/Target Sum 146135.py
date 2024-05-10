# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def findtarget(i, _sum):
            if i == n:
                if _sum == target:
                    return 1
                return 0
            
            if (i, _sum) not in memo:
                res = findtarget(i+1, _sum-nums[i]) + findtarget(i+1, _sum+nums[i])
                memo[(i, _sum)] = res
            return memo[(i, _sum)]

        return findtarget(0,0)


            