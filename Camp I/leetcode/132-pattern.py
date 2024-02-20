class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        curMin = nums[0]
        for n in nums:
            while stack and stack[-1][0] <= n:
                stack.pop()
            if stack and n > stack[-1][1]:
                return True
            stack.append([n, curMin])
            curMin = min(curMin, n)
        return False