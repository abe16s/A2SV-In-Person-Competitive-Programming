# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxi = []
        mini = []
        l = 0
        longest = 0
        for r in range(len(nums)):
            heappush(maxi, [-nums[r], r])
            heappush(mini, [nums[r], r])
            while -maxi[0][0] - mini[0][0] > limit:
                while maxi[0][1] <= l:
                    heappop(maxi)
                while mini[0][1] <= l:
                    heappop(mini)
                l += 1
            longest = max(longest, r-l+1)
        return longest