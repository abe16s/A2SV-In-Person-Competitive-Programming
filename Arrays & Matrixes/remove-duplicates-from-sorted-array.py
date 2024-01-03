class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 1
        temp = nums[0]
        while j < len(nums):
            while j < len(nums) and nums[j] == temp:
                j += 1
            if j < len(nums):
                temp = nums[j]
                nums[i] = nums[j]
                i += 1
                j += 1
        return i
            
         