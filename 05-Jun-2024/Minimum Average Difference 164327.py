# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ps = []
        rs = 0
        for i in range(n):
            rs += nums[i]
            ps.append(rs)
            
        min_avg_diff = float(inf)
        min_idx = -1
        for i in range(n):
            if i == n-1:
                cur = abs((ps[i]//(i+1)))
            else:
                cur = abs(ps[i]//(i+1) - (rs-ps[i]) // (n-i-1))

            if cur < min_avg_diff:
                min_avg_diff = cur
                min_idx = i
        return min_idx