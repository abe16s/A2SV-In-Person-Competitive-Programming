# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, n: int) -> int:
        if n == 0:
            return 1
        return 2 ** (math.floor(math.log(n, 2))+1)  - 1 - n