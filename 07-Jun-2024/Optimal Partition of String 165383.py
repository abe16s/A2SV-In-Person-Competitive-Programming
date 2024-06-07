# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        window = set()
        substrings = 0
        for c in s:
            if c in window:
                window.clear()
                substrings += 1
            window.add(c)
        return substrings + 1