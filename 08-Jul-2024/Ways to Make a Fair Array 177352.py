# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        suffix = nums[::]
        prefix = nums[::]
        for i in range(n-3, -1, -1):
            suffix[i] += suffix[i+2]
            prefix[n-i-1] += prefix[n-i-3]
        indices = 0
        even = odd = 0
        for i in range(n):
            e, o = even, odd
            if i % 2 == 0:
                if i + 1 < n:
                    e += suffix[i+1]
                if i + 2 < n:
                    o += suffix[i+2]
                even = prefix[i]
            else:
                if i + 1 < n:
                    o += suffix[i+1]
                if i + 2 < n:
                    e += suffix[i+2]
                odd = prefix[i]
            if e == o:
                indices += 1
            
        return indices