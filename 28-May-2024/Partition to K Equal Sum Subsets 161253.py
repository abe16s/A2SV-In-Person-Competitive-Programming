# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % k:
            return False
        target = total//k

        @cache
        def dp(mask, curSum):
            if mask == (1<<n)-1: 
                return curSum == target
            
            if curSum == target:
                return dp(mask, 0)

            for i in range(n):
                if not mask & (1<<i):
                    if curSum+nums[i] > target:
                        continue
                    if dp(mask|(1<<i), curSum+nums[i]):
                        return True

        return dp(0,0)
