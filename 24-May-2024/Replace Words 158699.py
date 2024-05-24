# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def addWord(self, word, root) -> None:
        current = root
        for ch in word:
            if ch not in current:
                current[ch] = {"is_end": False}
            current = current[ch]
        current["is_end"] = True

    def search(self, word, root) -> str:
        current = root
        for c in range(len(word)):
            if current["is_end"]:
                return word[:c]
            if word[c] not in current:
                break
            current = current[word[c]]  
        return word   
        
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = {"is_end": False}
        for word in dictionary:
            self.addWord(word, roots)

        sentence = sentence.split(" ")
        for i in range(len(sentence)):
            sentence[i] = self.search(sentence[i], roots)
        
        return " ".join(sentence)