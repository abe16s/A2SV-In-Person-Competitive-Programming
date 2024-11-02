# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy = nums[:]
        k = k % len(nums)
        temp = nums[-k:]
        for i in range(len(nums)-k):
            nums[i+k] = copy[i]
        for j in range(k):
            nums[j] = temp[j]