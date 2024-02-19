class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        j = 0
        stack = []
        n = len(nums)
        while j < 2*n:
            while stack and nums[j%n] > nums[stack[-1]]:
                if stack[-1] >= n:
                    return ans
                ans[stack.pop()] = nums[j%n]
            stack.append(j%n)
            j += 1
        
        return ans