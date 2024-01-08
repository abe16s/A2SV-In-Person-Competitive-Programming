class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _max = sum(nums[0:k])
        prev = _max
        r = k
        while r < len(nums):
            prev += nums[r] - nums[r-k]
            _max = max(_max, prev)
            r += 1
        
        return _max/k