# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        i, n = 0, len(s)
        stack = []
        while i < n:
            cur = "" 
            while i < n and (s[i].isnumeric() or s[i] == " "):
                if s[i] != "":
                    cur += s[i]
                    i += 1
            if stack and stack[-1] == "*":
                stack.pop()
                stack.append(stack.pop()*int(cur))
            elif stack and stack[-1] == "/":
                stack.pop()
                stack.append(stack.pop()//int(cur))
            else:
                stack.append(int(cur))
            if i < n:
                stack.append(s[i])
                i += 1
        rs = stack[0]
        for i in range(2, len(stack), 2):
            if stack[i-1] == "-":
                stack[i] *= -1
            rs += stack[i]
        return rs
