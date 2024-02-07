class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ps1 = [0] * (len(nums)+1)
        ps2 = [0] * (len(nums)+1)
        rs = 0
        total = sum(nums)
        for i in range(len(nums)):
            rs += nums[i]
            ps1[i+1] = rs
            ps2[i] = total-rs
        for i in range(len(nums)):
            if ps1[i] ==  ps2[i]:
                return i
        return -1