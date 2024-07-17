# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        visited = set()
        i = j = 0
        while i < len(s):
            while j < len(s) and s[j] not in visited:
                visited.add(s[j])
                j += 1 
                maxi = max(maxi, j-i)      
            if j < len(s):
                while s[i] != s[j]:
                    visited.remove(s[i])
                    i += 1
            i += 1
            j += 1
        return maxi       