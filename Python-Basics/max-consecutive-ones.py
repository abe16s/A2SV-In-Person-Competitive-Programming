class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i]:
                cur += 1
                maxi = max(maxi, cur)
            else:
                cur = 0
        return maxi