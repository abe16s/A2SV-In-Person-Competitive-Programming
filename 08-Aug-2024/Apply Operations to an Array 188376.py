# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zeros = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        print(nums)
        j = 0
        for i in range(len(nums)):
            if nums[i] and j < len(zeros): 
                nums[zeros[j]], nums[i] = nums[i], nums[zeros[j]]
                j += 1
                zeros.append(i)
            elif nums[i] == 0:
                zeros.append(i)
        return nums