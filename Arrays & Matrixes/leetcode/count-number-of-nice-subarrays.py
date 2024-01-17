class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nice = 0
        odds = 0
        i = 0
        j = 0
        subs = 0
        while j < len(nums):
            if (nums[j] % 2):
                odds += 1
                subs = 0
            while i < len(nums) and odds==k:
                if nums[i] % 2:
                    odds -= 1
                i += 1
                subs += 1
            nice += subs
            j += 1
        return nice