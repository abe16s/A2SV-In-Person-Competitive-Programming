# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        f1 = 0
        f2 = 1
        while n >= 2:
            f1, f2 = f2, f2+f1
            n -= 1
        return f2