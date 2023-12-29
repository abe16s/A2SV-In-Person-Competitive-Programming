class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        total = 0
        while i < len(nums):
            cur = nums[i]
            j = i + 1
            while j < len(nums) and nums[j] == cur:
                j += 1
            if j < len(nums):
                total += j 
            i = j
        return total