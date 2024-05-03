# Problem: Length of the Longest Valid Substring - https://leetcode.com/problems/length-of-the-longest-valid-substring/

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        r = len(word) - 1
        ans = 0
        for l in range(len(word)-1, -1, -1):
            for k in range(l, min(l+10, r+1)):
                if word[l:k+1] in forbidden:
                    r = k-1
                    break
            ans = max(ans, r-l+1)
        return ans