# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l] if 0 <= l < len(nums) else nums[0]