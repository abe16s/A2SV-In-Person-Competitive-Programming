class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            pos = self.myPow(x,-n)
            return 1/pos
        if n == 0:
            return 1
        if n == 1:
            return x
        y = self.myPow(x,n//2)
        return y * y if n % 2 == 0 else y * y * x