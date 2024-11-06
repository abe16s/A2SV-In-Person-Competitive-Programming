# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0
        curString = []
        for c in s:
            if c.isdigit():
                curNum = curNum * 10 + int(c)
            elif c.isalpha():
                curString.append(c)
            elif c == "[":
                stack.append(curString)
                stack.append(curNum)
                curNum = 0
                curString = []
            else:
                freq = stack.pop()
                prevString = stack.pop()
                curString = prevString + freq * curString
        
        return "".join(curString)