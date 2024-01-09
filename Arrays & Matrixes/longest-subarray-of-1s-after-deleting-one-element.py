class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        end = 0
        ctr = 0
        window = 0
        idx = 0 
        while end < len(nums):
            if nums[end]:
                end += 1
                continue
            ctr += 1
            if ctr == 1:
                idx = end
            if ctr == 2:
                window = max(window, end-start-1)
                start = idx + 1
                idx = end
                ctr -= 1
            end += 1
        if ctr <= 1:
            window = max(window, end-start-1)
        return window
               
