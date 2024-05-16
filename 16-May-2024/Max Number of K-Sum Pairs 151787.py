# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        output = 0
        while l < r:
            cur = nums[l] + nums[r]
            if cur == k:
                l += 1
                r -= 1
                output += 1
            elif cur < k:
                l += 1
            else:
                r -= 1
        return output