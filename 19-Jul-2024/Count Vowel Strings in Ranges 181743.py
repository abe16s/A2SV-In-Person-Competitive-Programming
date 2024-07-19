# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ps = [0]
        for w in words:
            ps.append(ps[-1]+int(w[0] in "aeiou" and w[-1] in "aeiou"))

        return [ps[r+1]-ps[l] for l, r in queries]