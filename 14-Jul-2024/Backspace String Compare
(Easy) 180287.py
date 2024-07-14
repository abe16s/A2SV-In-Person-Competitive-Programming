# Problem: Backspace String Compare
(Easy) - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for i in s:
            if i != "#":
                s_stack.append(i)
            elif s_stack:
                s_stack.pop()
        for j in t:
            if j != "#":
                t_stack.append(j)
            elif t_stack:
                t_stack.pop()
        return t_stack == s_stack 
