class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cout = []
        rs = 0
        for i in range(len(nums)):
            rs += nums[i]
            cout.append(rs)
        return cout