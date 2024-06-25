# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        def check(f):
            ctr = 1
            prev = position[0]
            for i in range(1,n):
                if position[i] - prev >= f:
                    ctr += 1
                    prev = position[i]
            return ctr >= m

        l = 0
        r = position[-1] - position[0]
        while l <= r:
            mid = l + (r-l) // 2
            if check(mid):
                l = mid+1
            else:
                r = mid-1
        return l - 1
            