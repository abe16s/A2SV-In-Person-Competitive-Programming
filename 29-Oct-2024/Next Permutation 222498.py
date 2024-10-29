# Problem: Next Permutation - https://leetcode.com/problems/next-permutation/description/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(l, r):
            while l <= r:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                r -= 1

        index = len(nums)-2
        while index >= 0 and nums[index] >= nums[index+1]:
            index -= 1
        
        if index >= 0:
            other_idx = -1
            i = len(nums)-1
            while i > index:
                if (other_idx == -1 or nums[other_idx] > nums[i]) and nums[i] > nums[index]:
                    other_idx = i 
                i -= 1
            nums[index], nums[other_idx] = nums[other_idx], nums[index]
        
        reverse(index+1, len(nums)-1)