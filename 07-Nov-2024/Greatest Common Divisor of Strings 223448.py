# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        factor = str1 if len(str1) < len(str2) else str2
        for i in range(min(len(str1), len(str2))-1,-1,-1):
            if len(str1) % len(factor) == 0 and len(str2) % len(factor) == 0:
                if factor * (len(str1) // len(factor)) == str1 and factor * (len(str2) // len(factor)) == str2:
                    break
            factor = factor[:-1]

        return factor 
