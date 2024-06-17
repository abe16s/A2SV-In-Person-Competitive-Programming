# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c))
        while l <= r:
            cur = l**2 + r**2
            if cur == c:
                return True
            elif cur > c:
                r -= 1
            else:
                l += 1
        
        return False