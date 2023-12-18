class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        n = len(s)
        list_s = list(s)
        while i < n:
            l = i
            r = min(len(s), l+k) - 1
            while l < r:
                list_s[r], list_s[l] = list_s[l], list_s[r]
                l += 1
                r -= 1
            i += 2*k
        return "".join(list_s)