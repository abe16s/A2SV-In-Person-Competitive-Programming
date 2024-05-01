# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cur = x ^ y
        if cur == 0:
            return 0
        bit = []
        while cur > 1:
            bit.append(cur%2)
            cur //= 2
        bit.append(1)
        return bit.count(1)