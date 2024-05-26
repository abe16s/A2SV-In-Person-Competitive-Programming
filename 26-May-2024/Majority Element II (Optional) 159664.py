# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        atleast = len(nums)//3
        output = set()
        for num in nums:
            if num not in output and nums.count(num) > atleast:
                output.add(num)
        return list(output)