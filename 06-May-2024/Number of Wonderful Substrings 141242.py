# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        prefix = defaultdict(int)
        prefix[0] += 1
        ans = 0
        freq = 0
        for l in word:
            cur = ord(l)-97
            freq ^= 1 << cur
            ans += prefix[freq]
            for n in range(10):
                ans += prefix[freq ^ 1 << n]
            prefix[freq] += 1
        return ans


