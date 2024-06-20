# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = float("inf")
        for j in strs:
            i = min(i, len(j))
        cout = ""
        for k in range(i):
            cur = strs[0][k]
            flag = False
            for l in strs:
                if l[k] != cur:
                    flag = True
                    break
            if flag:
                break
            cout += cur
        return cout