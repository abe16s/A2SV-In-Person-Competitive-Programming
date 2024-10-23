# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ramp = 0
        stack = [0]
        for i in range(1, len(nums)):
            if nums[stack[-1]] > nums[i]:
                stack.append(i)
            else:
                l, r = 0, len(stack)-1
                while l <= r:
                    mid = l + (r-l)//2
                    if nums[stack[mid]] <= nums[i]:
                        r = mid-1
                    else:
                        l = mid+1
                ramp = max(ramp, i-stack[l])
        return ramp