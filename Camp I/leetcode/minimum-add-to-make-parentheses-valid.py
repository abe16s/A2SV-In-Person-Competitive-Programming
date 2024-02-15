class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ctr = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif stack:
                stack.pop()
            else:
                ctr += 1
        return ctr + len(stack)

        