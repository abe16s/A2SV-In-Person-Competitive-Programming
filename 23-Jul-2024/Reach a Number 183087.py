# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        l = 1
        r = 10**9
        while l <= r:
            mid = l + (r-l)//2
            cur = mid * (mid+1) // 2
            if cur == target:
                return mid
            elif cur < target:
                l = mid+1
            else:
                r = mid-1
        if ((l*(l+1)//2)-target) % 2:
            if l % 2:
                l += 2
            else:
                l += 1
        return l