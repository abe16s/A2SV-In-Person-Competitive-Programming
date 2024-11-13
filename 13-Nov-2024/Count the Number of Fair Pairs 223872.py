# Problem: Count the Number of Fair Pairs - https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        l = pairs = 0
        for r in range(len(nums)-1, -1, -1):
            temp = nums[r]
            nums.pop()
            pairs += bisect_right(nums, upper-temp) - bisect_left(nums, lower-temp) 
        
        return pairs
