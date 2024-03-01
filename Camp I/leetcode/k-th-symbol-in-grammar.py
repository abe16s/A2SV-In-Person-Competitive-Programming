class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def recurse(n, k):
            if n == 1:
                return 0
            prev = recurse(n-1, (k)%(2**(n-1)//2))
            if k >= (2**(n-1)//2):
                return 1-prev
            else:
                return prev
        return recurse(n, k-1)
