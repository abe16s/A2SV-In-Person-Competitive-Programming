class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        total = 0
        for i in s:
            if i == "(":
                stack.append(total)
                total = 0
            else:
                total = stack.pop() + max(total*2, 1)
        return total