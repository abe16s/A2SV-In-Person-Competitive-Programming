# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = maxLen = 0
        if len(s) < 2:
            return s
        def extend(j,k):
            nonlocal maxLen
            nonlocal start
            while j >= 0 and k < len(s) and s[j] == s[k]:
                j -= 1
                k += 1
            if maxLen < k-j-1:
                start = j + 1
                maxLen = k-j-1

        for i in range(len(s)):
            extend(i, i)
            extend(i, i+1)
        
        return s[start : start + maxLen]



