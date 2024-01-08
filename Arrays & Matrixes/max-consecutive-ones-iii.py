class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        i = 0
        maxi = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeros += 1
            while zeros > k:
                if nums[i] == 0:
                    zeros -= 1
                i += 1
            maxi = max(maxi, j-i+1)
        return maxi