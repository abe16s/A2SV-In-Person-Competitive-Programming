# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for j in range(1,n+1):
            if j%3 == 0 and j%5 == 0:
                out.append("FizzBuzz")
            elif j%3 == 0:
                out.append("Fizz")
            elif j%5 == 0:
                out.append("Buzz")
            else:
                out.append(str(j))
        return out