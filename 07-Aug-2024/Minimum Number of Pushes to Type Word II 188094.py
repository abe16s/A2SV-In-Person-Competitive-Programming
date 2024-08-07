# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        k = sorted(c.keys(), key = lambda x: c[x], reverse = True)
        pushes = 0
        for i in range(len(k)):
            pushes += (i // 8 + 1) * c[k[i]]

        return pushes