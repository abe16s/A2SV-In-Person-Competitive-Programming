class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possible_values = {}
        for i in range(len(nums)):
            if nums[i] in possible_values:
                return [i,possible_values[nums[i]]]
            possible_values[target - nums[i]] = i
        

