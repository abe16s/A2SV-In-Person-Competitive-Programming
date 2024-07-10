# Problem: Find All Good Indices - https://leetcode.com/problems/find-all-good-indices/

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        increasing = [1] * n 
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                increasing[i] += increasing[i-1]
        decreasing = [1] * n
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                decreasing[i] += decreasing[i+1]
        good = []
        for i in range(k, n-k):
            if increasing[i-1] >= k and decreasing[i+1] >= k:
                good.append(i)
        return good