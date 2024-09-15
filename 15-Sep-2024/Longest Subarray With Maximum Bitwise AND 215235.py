# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi = [0,0] # number, length
        i = 0
        while i < len(nums):
            ctr = 0
            temp = nums[i]
            while i < len(nums) and nums[i] == temp:
                ctr += 1
                i += 1
            if [temp, ctr] > maxi:
                maxi = [temp, ctr]

        return maxi[1]