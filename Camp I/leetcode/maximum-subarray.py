class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        rs = 0
        cout = -float("inf")
        mini = 0
        for i in range(len(nums)):
            rs += nums[i]
            cout = max(cout, rs-mini)
            mini = min(mini, rs)
        
        return cout