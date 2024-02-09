class Solution:
    def minimumSteps(self, s: str) -> int:
        rs = 0
        ctr = 0
        for i in range(len(s)):
            if s[i] == "1":
                rs += 1
            else:
                ctr += rs
        return ctr