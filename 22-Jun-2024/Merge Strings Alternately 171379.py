# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0 
        cout = ""
        while i < min(len(word1), len(word2)):
            cout += word1[i]
            cout += word2[i]
            i += 1
        cout += word1[i:]
        cout += word2[i:]
        return cout