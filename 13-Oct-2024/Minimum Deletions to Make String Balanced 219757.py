# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0
        bcount = 0
        for l in s:
            if l == 'a':
                res = min(res + 1, bcount)
            else:
                bcount += 1
        return res