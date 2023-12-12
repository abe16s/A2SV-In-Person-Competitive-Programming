class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i] in s:
                s.remove(nums[i])
                r = nums[i] + 1
                while r in s:
                    s.remove(r)
                    r += 1
                l = nums[i]-1
                while l in s:
                    s.remove(l)
                    l -= 1
                cur = r - l - 1
                longest = max(longest, cur)
        return longest