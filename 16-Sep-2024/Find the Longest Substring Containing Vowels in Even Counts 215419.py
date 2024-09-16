# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"
        bitmask = 0
        ps = defaultdict(int)
        ps[0] = -1
        ans = 0
        for i in range(len(s)):
            x = vowels.find(s[i])
            if x != -1:
                bitmask ^= (1<<x)
            ps.setdefault(bitmask, i)
            ans = max(ans, i-ps[bitmask])
        return ans


        return 0