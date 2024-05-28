# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        maxLength = 0
        curCost = 0
        l = 0
        for r in range(len(s)):
            curCost += abs(ord(s[r])-ord(t[r]))
            if curCost <= maxCost:
                maxLength = max(maxLength, r-l+1)
            while curCost > maxCost:
                curCost -= abs(ord(s[l])-ord(t[l]))
                l += 1
        
        return maxLength