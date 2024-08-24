# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:
        prev_num = -1
        prev_den = -1
        i = 0
        n = len(expression)
        while i < n:
            cur_num = 1
            if expression[i] == "-":
                cur_num *= -1
                i += 1
            elif expression[i] == "+":
                i += 1
            temp = ""
            while i < n and expression[i].isnumeric():
                temp += expression[i]
                i += 1
            cur_num *= int(temp)
            i += 1
            temp = ""
            cur_den = 1
            while i < n and expression[i].isnumeric():
                temp += expression[i]
                i += 1
            cur_den *= int(temp)
            if prev_num == prev_den == -1:
                prev_num = cur_num
                prev_den = cur_den
                continue
            prev_num = (prev_num * cur_den) + (prev_den * cur_num)
            prev_den = prev_den * cur_den
            g = math.gcd(prev_num, prev_den)
            while g > 1:
                prev_num //= g
                prev_den //= g
                g = math.gcd(prev_num, prev_den)

        return str(prev_num)+"/"+str(prev_den)


            
            
