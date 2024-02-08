class Solution:
    def maxScore(self, s: str) -> int:
        ps0 = []
        rs = 0
        for c in s:
            if c == "0":
                rs += 1
            ps0.append(rs)

        ps1 = [0] * len(s)
        rs = 0
        for i in range(len(s)-1,-1,-1):
            ps1[i] = rs
            if s[i] == "1":
                rs += 1
        
        maxi = 0
        for i in range(len(s)-1):
            maxi = max(maxi, ps0[i] + ps1[i])

        return maxi
