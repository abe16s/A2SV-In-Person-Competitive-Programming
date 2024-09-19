# Problem: Find Indices With Index and Value Difference II - https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums) 
        j1 = 0
        j2 = 0

        for i in range(indexDifference, n):
            if abs(nums[i] - nums[j1]) >= valueDifference:
                return [i, j1]
            elif abs(nums[i] - nums[j2]) >= valueDifference:
                return [i, j2]
            
            if i-indexDifference+1 < len(nums):
                if nums[i-indexDifference+1] < nums[j1]:
                    j1 = i-indexDifference+1
                if nums[i-indexDifference+1] > nums[j2]:
                    j2 = i-indexDifference+1

        return [-1, -1] 