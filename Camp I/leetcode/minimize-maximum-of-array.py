class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        rs = nums[0]
        for i in range(1,len(nums)):
            rs += nums[i]
            res = max(res, math.ceil(rs/(i+1)))
        return res