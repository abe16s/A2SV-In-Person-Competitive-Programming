# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        low, high, n = min(nums), max(nums), len(nums)
        if n <= 2 or high == low: 
            return high - low
        bucket = defaultdict(list)
        for num in nums:
            if num == high:
                idx = n-2
            else:
                idx = (num - low) * (n-1)//(high-low)
            bucket[idx].append(num)
        cands = [[min(bucket[i]), max(bucket[i])] for i in range(n-1) if bucket[i]]
        return max(y[0]-x[1] for x,y in zip(cands, cands[1:]))