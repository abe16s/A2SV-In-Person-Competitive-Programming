# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        current_window = defaultdict(int)
        current_sum = 0
        maximum_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            current_window[nums[right]] += 1
            if right >= k:
                current_window[nums[right-k]] -= 1
                current_sum -= nums[right-k]
                if current_window[nums[right-k]] == 0:
                    current_window.pop(nums[right-k])

            if len(current_window) == k:
                maximum_sum = max(maximum_sum, current_sum)
        
        return maximum_sum