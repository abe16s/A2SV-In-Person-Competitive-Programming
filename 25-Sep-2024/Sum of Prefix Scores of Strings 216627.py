# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class Solution:
    def addWord(self, word, root) -> None:
        current = root
        for ch in word:
            current["freq"] += 1
            if ch not in current:
                current[ch] = {"freq": 0}
            current = current[ch]
        current["freq"] += 1

    def search(self, word, root) -> str:
        current = root
        count = 0
        for c in range(len(word)):
            current = current[word[c]] 
            count += current["freq"]
        return count 

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = {"freq": 0}
        for word in words:
            self.addWord(word, root)
        
        ans = []
        for word in words:
            ans.append(self.search(word, root))
        return ans

        