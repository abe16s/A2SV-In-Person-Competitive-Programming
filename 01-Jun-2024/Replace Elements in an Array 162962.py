# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            dic[num] = idx 
        for op in operations:
            dic[op[1]] = dic[op[0]]
            dic.pop(op[0])
        for k, v in dic.items():
            nums[v] = k
        return nums