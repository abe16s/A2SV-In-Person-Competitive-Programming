# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [1]
        for i in range(len(nums)-1):
            before.append(before[-1] * nums[i])
         
        after = [1]
        for j in range(len(nums)-1, 0, -1):
            after.append(after[-1] * nums[j])

        cout = [(before[k] * after[len(nums)-1-k]) for k in range(len(nums))]
        return cout