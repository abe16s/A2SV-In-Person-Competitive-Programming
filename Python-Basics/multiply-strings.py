class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = 0
        b = 0
        bet = 1
        for i in range(len(num1)-1,-1,-1):
            a += (bet*int(num1[i]))
            bet *= 10
        bet = 1
        for i in range(len(num2)-1,-1,-1):
            b += (bet*int(num2[i]))
            bet *= 10
        return str(a * b)
