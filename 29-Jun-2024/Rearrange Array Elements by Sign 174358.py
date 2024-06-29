# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        for i in range(len(positives)):
            nums[i*2] = positives[i]
            nums[i*2+1] = negatives[i]
        return nums