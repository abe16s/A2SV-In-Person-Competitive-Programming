# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = 0
        ctr = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack += 1
            elif stack > 0:
                stack -= 1
            else:
                ctr += 1
        return ctr + stack
        