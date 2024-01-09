class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum = float("inf")
        left = 0
        s = 0

        for right in range(len(nums)):
            s += nums[right]
            while s >= target:
                minimum = min(minimum, right - left + 1)
                s -= nums[left]
                left += 1
                
        return minimum if minimum != float("inf") else 0
        