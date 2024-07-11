# Problem: Reverse Substrings Between Each Pair of Parentheses - https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for c in s:
            if c == "(":
                stack.append("")
            elif c == ")":
                inside = stack.pop()
                stack[-1]+= inside[::-1]
            else:
                stack[-1] += c

        return stack[0]
