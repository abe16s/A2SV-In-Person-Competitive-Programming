# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        found = set()
        ctr = 0
        maxi = nums[0]
        for n in nums:
            if n in found:
                maxi = max(maxi, n) + 1
                ctr += maxi - n
                found.add(maxi)
            else:
                found.add(n)
        return ctr