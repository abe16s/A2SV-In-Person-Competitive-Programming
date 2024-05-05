# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        letters = [0] * len(words)
        for w in range(len(words)):
            for ltr in words[w]:
                letters[w] |= 1 << (ord(ltr)-97)

        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not letters[i] & letters[j]:
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans