# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        wind = 0
        freq = 1
        j = 0
        for i in range(len(nums)):
            while ((i-j)*nums[i])-wind > k:
                wind -= nums[j]
                j += 1
            wind += nums[i]
            freq = max(freq, i-j+1)
        return freq
