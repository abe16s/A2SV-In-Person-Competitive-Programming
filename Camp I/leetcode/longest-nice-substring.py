class Solution(object):
    def longestNiceSubstring(self, s):
        if len(s) < 2:
            return ""
        chars = set(s)
        for i in range(len(s)):
            if not(s[i].upper() in chars and s[i].lower() in chars):
                sub1 = self.longestNiceSubstring(s[:i])
                sub2 = self.longestNiceSubstring(s[i+1:])
                return sub1 if len(sub1) >= len(sub2) else sub2
        return s