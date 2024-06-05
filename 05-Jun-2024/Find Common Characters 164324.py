# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        commons = [float("inf")]*26
        for i in range(len(words)):
            C = Counter(words[i])
            for ch in range(26):
                commons[ch] = min(commons[ch], C[chr(97+ch)])

        cout = []
        for i in range(26):
            cout.extend([chr(97+i) for _ in range(commons[i])])
        return cout
