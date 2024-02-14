class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ctr = 0
        rs = 0
        j = 0
        i = 0
        while i <= n:
            while j < len(nums) and i >= nums[j]:
                rs += nums[j]
                j += 1
            if rs < i:
                ctr += 1
                rs += i
            i = rs+1
        return ctr
