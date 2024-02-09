class Solution:
    def numberOfWays(self, s: str) -> int:
        n0 = [0]
        n1 = [0]
        for c in s:
            if c == "0":
                n0.append(n0[-1]+1)
                n1.append(n1[-1])
            else:
                n1.append(n1[-1]+1)
                n0.append(n0[-1])
        n01 = [0]
        n10 = [0]
        for i in range(len(s)):
            if s[i] == "0":
                n10.append(n10[-1]+n1[i+1])
                n01.append(n01[-1])
            else:
                n01.append(n01[-1]+n0[i+1])
                n10.append(n10[-1])
        ctr = 0
        for i in range(len(s)):
            if s[i] == "0":
                ctr += n01[i+1]
            else:
                ctr += n10[i+1]
        return ctr
