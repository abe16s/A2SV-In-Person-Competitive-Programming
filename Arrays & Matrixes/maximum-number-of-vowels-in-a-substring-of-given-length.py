class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        i = 0 
        j = 0
        maxi = 0
        cur = 0
        while j < len(s):
            if j >= k:
                if s[i] in vowels:
                    cur -= 1
                i += 1
            if s[j] in vowels:
                cur += 1
            maxi = max(maxi, cur)
            j += 1
        return maxi
            