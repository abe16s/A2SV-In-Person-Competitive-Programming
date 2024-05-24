# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def addWord(self, word, root) -> None:
        current = root
        for ch in word:
            if ch not in current:
                current[ch] = {"is_end": False}
            current = current[ch]
        current["is_end"] = True

    def search(self, word, root) -> bool:
        current = root
        for c in range(len(word)):
            if not current["is_end"]:
                return False
            current = current[word[c]]  
        return True  

    def longestWord(self, words: List[str]) -> str:
        root = {"is_end": True}
        for word in words:
            self.addWord(word, root)

        longest = ""
        for word in words:
            if self.search(word, root):
                if len(word) > len(longest):
                    longest = word
                elif len(word) == len(longest):
                    longest = min(word, longest)
        return longest