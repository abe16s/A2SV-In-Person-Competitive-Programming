class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ps = [0] * (len(nums)+1)
        for s,e in requests:
            ps[s] += 1
            ps[e+1] -= 1
        
        for i in range(1,len(ps)):
            ps[i] += ps[i-1]

        ps.pop()
        ps.sort()
        nums.sort()

        cout = 0
        for i in range(len(nums)):
            cout += (nums[i] * ps[i])

        return cout  % (10**9 + 7)