# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 2**32 - 1
        carry = 0 
        while (b & mask) != 0:
            carry = (a&b) << 1
            a = a^b
            b = carry
        return (a & mask) if b > 0 else a
