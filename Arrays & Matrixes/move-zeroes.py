class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        n = 0
        while n < len(nums) and z < len(nums):
            if nums[z] == 0:
                n = z
                while n < len(nums) and nums[n] == 0:
                    n += 1
                if n < len(nums):
                    nums[z], nums[n] = nums[n], nums[z]
            z += 1
