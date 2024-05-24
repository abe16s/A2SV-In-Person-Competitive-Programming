# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary:

    def __init__(self):
        self.root = {"is_end": False}

    def addWord(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current:
                current[ch] = {"is_end": False}
            current = current[ch]
        current["is_end"] = True
            
    def search(self, word: str) -> bool:
        queue = deque([self.root])
        for ch in word:
            if not queue:
                break
            for q in range(len(queue)):
                current = queue.popleft()
                if ch == ".":
                    for child in current:
                        if child != "is_end":
                            queue.append(current[child])
                elif ch in current:
                    queue.append(current[ch])

        for q in queue:
            if q["is_end"]:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)