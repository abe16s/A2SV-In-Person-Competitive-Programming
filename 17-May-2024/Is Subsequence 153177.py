# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in s:
            flag = False
            while i < len(t):
                i += 1
                if t[i-1] == c:
                    flag = True
                    break
            if not flag:
                return False
        return True