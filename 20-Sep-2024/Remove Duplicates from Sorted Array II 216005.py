# Problem: Remove Duplicates from Sorted Array II - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 1
        temp = -float("inf")
        while j < len(nums):
            while j < len(nums) and nums[j] == temp:
                j += 1
            if j < len(nums):
                nums[i] = nums[j]
                if nums[i] == nums[i-1]:
                    temp = nums[i]
                i += 1
                j += 1               
        return i