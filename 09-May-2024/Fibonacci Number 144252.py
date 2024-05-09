# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        store = {0:0, 1:1}
        def fn(n):
            if n in store:
                return store[n] 
            cur = fn(n-1) + fn(n-2)
            store[n] = cur
            return cur
        return fn(n)