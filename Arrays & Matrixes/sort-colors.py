class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        min_idx = 0
        for i in range(3):
            for j in range(len(nums)):
                if i == nums[j]:
                    nums[min_idx], nums[j] = nums[j], nums[min_idx]
                    min_idx += 1
        return nums