# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(3):
            for j in range(len(nums)):
                if nums[j] == i:
                    nums[k], nums[j] = nums[j], nums[k]
                    k += 1
        return nums