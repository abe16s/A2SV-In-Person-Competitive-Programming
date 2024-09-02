# Problem: Vowel of All Substring - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        vowels = "aeiou"
        ans = 0
        n = len(word)
        for i in range(len(word)):
            if word[i] in vowels:
                ans += (n-i) * (i) + (n-i) 

        return ans