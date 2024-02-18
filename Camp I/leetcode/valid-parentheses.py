class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(":")", "{":"}","[":"]"}
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            elif not stack or dic[stack.pop()] != i:
                return False
        return not stack

                