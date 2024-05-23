# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode():
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not current.children[idx]:
                current.children[idx] = TrieNode()
            current = current.children[idx]
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not current.children[idx]:
                return False
            current = current.children[idx]      
        return current.is_end

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for c in prefix:
            idx = ord(c) - ord("a")
            if not current.children[idx]:
                return False
            current = current.children[idx] 
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)