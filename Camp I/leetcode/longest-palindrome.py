class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        evens = 0
        odd = 0
        for k in c:
            if c[k] >= 2:
                evens += c[k]
                if c[k] % 2:
                    evens -= 1
            if c[k] % 2:
                odd = 1
        return evens + odd
