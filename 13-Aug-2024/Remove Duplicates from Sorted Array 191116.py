# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        found = set()
        i = 0
        j = 0
        while j < len(nums):
            while  j < len(nums) and nums[j] in found:
                j += 1
            if j == len(nums):
                break
            print(i,j)
            found.add(nums[j])
            nums[i] = nums[j]
            i += 1
        print(nums)
        return len(found) 
