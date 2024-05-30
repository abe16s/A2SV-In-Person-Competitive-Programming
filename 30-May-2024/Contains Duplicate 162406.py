# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = set()
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            dic.add(nums[i])
        return False