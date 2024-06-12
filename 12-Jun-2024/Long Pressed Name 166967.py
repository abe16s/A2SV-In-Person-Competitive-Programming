# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False
        j = 0
        prev = ""
        for i in range(0,len(name)):
            if j<len(typed) and typed[j] == name[i]:
                j += 1
                prev = name[i]
                continue
            while j < len(typed) and typed[j] == prev:
                j += 1
            if j == len(typed) or typed[j] != name[i]:
                return False
            j += 1
            prev = name[i]
        
        while j < len(typed) and typed[j] == prev:
            j += 1
        
        return True if j == len(typed) else False


            